def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_pairs = []
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1 = words_list[i].lower()
            word2 = words_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1) == sorted(word2)):
                anagram_pairs.append((word1, word2))
    return len(anagram_pairs) <= 5