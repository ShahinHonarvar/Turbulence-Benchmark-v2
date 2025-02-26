def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        s1 = ''.join((c.lower() for c in s1 if c.isalpha()))
        s2 = ''.join((c.lower() for c in s2 if c.isalpha()))
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2))
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 73:
                    return False
    return True