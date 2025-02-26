def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_count = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            if are_anagrams(string_list[i], string_list[j]):
                anagram_count += 1
    return anagram_count >= 94