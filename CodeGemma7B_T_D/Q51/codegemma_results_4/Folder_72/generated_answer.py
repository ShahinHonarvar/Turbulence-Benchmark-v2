def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
    pairs = 0
    for anagram_group in anagrams.values():
        pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return pairs <= 188