def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and len(s1) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_pairs = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
    return anagram_pairs >= 209