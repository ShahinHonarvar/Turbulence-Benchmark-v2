def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        if len(word_lower) >= 3:
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    anagram_pairs = sum([count * (count - 1) // 2 for count in anagrams.values()])
    return anagram_pairs >= 70