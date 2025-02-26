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
        processed.add(s1_lower)
        s1_counter = Counter(s1_lower)
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            s2_lower = ''.join(filter(str.isalpha, s2.lower()))
            if s2_lower in processed:
                continue
            if len(s1_lower) == len(s2_lower) and s1_counter == Counter(s2_lower):
                anagram_count += 1
                processed.add(s2_lower)
                if anagram_count > 2:
                    return False
                break
    return True