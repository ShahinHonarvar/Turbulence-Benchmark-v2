from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3:
            continue
        s1_lower = ''.join(filter(str.isalpha, s1.lower()))
        if s1_lower in processed:
            continue
        s1_counter = Counter(s1_lower)
        processed.add(s1_lower)
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            s2_lower = ''.join(filter(str.isalpha, s2.lower()))
            if s1_lower != s2_lower and Counter(s2_lower) == s1_counter:
                anagram_count += 1
                if anagram_count > 36:
                    return False
    return True