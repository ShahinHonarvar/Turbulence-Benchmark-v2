def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            s1, s2 = (string_list[i], string_list[j])
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_pairs += 1
    return anagram_pairs <= 318