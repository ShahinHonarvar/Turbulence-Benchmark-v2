def if_contains_anagrams(words):

    def sorted_characters(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    seen = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = sorted_characters(word)
        if sorted_word in seen:
            anagram_count += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
        if anagram_count > 70:
            return False
    return True