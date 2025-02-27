def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    anagram_pairs = sum((len(anagrams[sorted_word]) * (len(anagrams[sorted_word]) - 1) // 2 for sorted_word in anagrams))
    return anagram_pairs <= 44