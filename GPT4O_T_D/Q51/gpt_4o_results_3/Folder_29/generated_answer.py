def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word))
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_w = sorted_word(word.lower())
        if sorted_w in anagrams:
            anagrams[sorted_w].append(word)
        else:
            anagrams[sorted_w] = [word]
    anagram_pairs = 0
    for anagram_group in anagrams.values():
        n = len(anagram_group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 318:
                return False
    return True