def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 0
            anagrams[sorted_word] += 1
    anagram_pairs = sum([count * (count - 1) // 2 for count in anagrams.values()])
    return anagram_pairs >= 75