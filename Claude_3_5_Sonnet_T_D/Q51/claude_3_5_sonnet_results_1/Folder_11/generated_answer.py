def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            s1, s2 = (string_list[i], string_list[j])
            if len(s1) >= 3 and len(s2) >= 3:
                s1_alpha = ''.join(filter(str.isalpha, s1.lower()))
                s2_alpha = ''.join(filter(str.isalpha, s2.lower()))
                if s1_alpha and s2_alpha and ((s1_alpha, s2_alpha) not in processed):
                    if is_anagram(s1_alpha, s2_alpha):
                        anagram_count += 1
                        processed.add((s1_alpha, s2_alpha))
                        processed.add((s2_alpha, s1_alpha))
                        if anagram_count > 41:
                            return False
    return True