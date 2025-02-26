from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if s1 in processed:
            continue
        s1_lower = ''.join(filter(str.isalpha, s1.lower()))
        if len(s1_lower) < 3:
            continue
        s1_counter = Counter(s1_lower)
        for s2 in string_list[i + 1:]:
            s2_lower = ''.join(filter(str.isalpha, s2.lower()))
            if len(s2_lower) < 3:
                continue
            if len(s1_lower) == len(s2_lower) and Counter(s2_lower) == s1_counter:
                anagram_count += 1
                processed.add(s2)
                if anagram_count > 30:
                    return False
        processed.add(s1)
    return True