def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    n = len(string_list)
    for i in range(n):
        for j in range(i + 1, n):
            s1, s2 = (string_list[i], string_list[j])
            if len(s1) >= 3 and len(s2) >= 3:
                s1_alpha = ''.join((c for c in s1.lower() if c.isalpha()))
                s2_alpha = ''.join((c for c in s2.lower() if c.isalpha()))
                if s1_alpha and s2_alpha and is_anagram(s1_alpha, s2_alpha):
                    anagram_count += 1
                    if anagram_count > 68:
                        return False
    return True