def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = ''.join(filter(str.isalpha, string_list[i]))
            s2 = ''.join(filter(str.isalpha, string_list[j]))
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_count += 1
                if anagram_count > 49:
                    return False
    return True