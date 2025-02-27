def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            anagram_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_pairs >= 10