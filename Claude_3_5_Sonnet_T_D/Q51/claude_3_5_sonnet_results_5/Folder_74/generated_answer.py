from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_strings = set()
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        if s_lower not in processed_strings:
            processed_strings.add(s_lower)
            s_sorted = ''.join(sorted(s_lower))
            for t in string_list:
                if s != t:
                    t_lower = ''.join(filter(str.isalpha, t.lower()))
                    if len(t_lower) >= 3 and ''.join(sorted(t_lower)) == s_sorted:
                        anagram_count += 1
                        if anagram_count > 57:
                            return False
    return True