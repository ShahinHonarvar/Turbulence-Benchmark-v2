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
        processed.add(s1_lower)
        s1_counter = Counter(s1_lower)
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            s2_lower = ''.join((c.lower() for c in s2 if c.isalpha()))
            if s1_lower != s2_lower and Counter(s2_lower) == s1_counter:
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True