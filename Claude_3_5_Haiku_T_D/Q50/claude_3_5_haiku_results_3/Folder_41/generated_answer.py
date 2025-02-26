def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and are_anagrams(string_list[i], string_list[j]):
                anagram_pairs += 1
    return anagram_pairs >= 75