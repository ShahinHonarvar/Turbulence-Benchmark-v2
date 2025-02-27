def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    normalized_lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for i in range(len(normalized_lst)):
        for j in range(i + 1, len(normalized_lst)):
            if is_anagram(normalized_lst[i], normalized_lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 46:
                    return False
    return True