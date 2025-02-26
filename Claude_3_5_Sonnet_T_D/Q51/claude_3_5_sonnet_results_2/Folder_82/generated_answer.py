def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            s1 = ''.join(filter(str.isalpha, string_list[i]))
            s2 = ''.join(filter(str.isalpha, string_list[j]))
            if len(s1) < 3 or len(s2) < 3:
                continue
            if (s1, s2) not in processed and (s2, s1) not in processed:
                if is_anagram(s1, s2):
                    anagram_count += 1
                    processed.add((s1, s2))
                    if anagram_count > 40:
                        return False
    return True