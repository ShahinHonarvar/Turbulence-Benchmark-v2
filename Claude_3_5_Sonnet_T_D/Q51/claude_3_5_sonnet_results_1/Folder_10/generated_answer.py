from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if s1 in processed:
            continue
        s1_cleaned = ''.join((c.lower() for c in s1 if c.isalpha()))
        if len(s1_cleaned) < 3:
            continue
        s1_counter = Counter(s1_cleaned)
        for s2 in string_list[i + 1:]:
            s2_cleaned = ''.join((c.lower() for c in s2 if c.isalpha()))
            if len(s2_cleaned) < 3:
                continue
            if len(s1_cleaned) == len(s2_cleaned) and Counter(s2_cleaned) == s1_counter:
                anagram_count += 1
                processed.add(s2)
            if anagram_count > 21:
                return False
    return True