def if_contains_anagrams(input_list):

    def is_anagram(s1, s2):
        s1 = ''.join(sorted((c.lower() for c in s1 if c.isalpha())))
        s2 = ''.join(sorted((c.lower() for c in s2 if c.isalpha())))
        return len(s1) >= 3 and len(s2) >= 3 and (s1 == s2)
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_count += 1
                if anagram_count > 67:
                    return False
    return True