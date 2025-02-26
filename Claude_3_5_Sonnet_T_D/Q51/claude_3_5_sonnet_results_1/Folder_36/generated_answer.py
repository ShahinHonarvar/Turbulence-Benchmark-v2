from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_strings = set()
    for s in string_list:
        s_cleaned = ''.join((char.lower() for char in s if char.isalpha()))
        if len(s_cleaned) < 3:
            continue
        if s_cleaned not in processed_strings:
            processed_strings.add(s_cleaned)
            s_sorted = ''.join(sorted(s_cleaned))
            for t in string_list:
                if s != t:
                    t_cleaned = ''.join((char.lower() for char in t if char.isalpha()))
                    if len(t_cleaned) < 3:
                        continue
                    t_sorted = ''.join(sorted(t_cleaned))
                    if s_sorted == t_sorted:
                        anagram_count += 1
                        if anagram_count > 25:
                            return False
    return True