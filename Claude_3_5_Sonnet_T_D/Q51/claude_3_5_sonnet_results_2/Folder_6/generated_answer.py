from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3:
            continue
        s1_lower = ''.join((c.lower() for c in s1 if c.isalpha()))
        if s1_lower in processed:
            continue
        s1_counter = Counter(s1_lower)
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            if len(s2) < 3:
                continue
            s2_lower = ''.join((c.lower() for c in s2 if c.isalpha()))
            if s2_lower in processed:
                continue
            if len(s1_lower) == len(s2_lower) and s1_counter == Counter(s2_lower):
                anagram_count += 1
                processed.add(s1_lower)
                processed.add(s2_lower)
                if anagram_count > 86:
                    return False
    return True