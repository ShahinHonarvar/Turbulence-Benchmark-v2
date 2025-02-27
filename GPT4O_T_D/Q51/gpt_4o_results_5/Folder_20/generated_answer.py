def if_contains_anagrams(words):

    def sorted_chars(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    seen_anagrams = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_chars(word)
            if sorted_word in seen_anagrams:
                anagram_count += seen_anagrams[sorted_word]
                seen_anagrams[sorted_word] += 1
            else:
                seen_anagrams[sorted_word] = 1
            if anagram_count > 131:
                return False
    return True