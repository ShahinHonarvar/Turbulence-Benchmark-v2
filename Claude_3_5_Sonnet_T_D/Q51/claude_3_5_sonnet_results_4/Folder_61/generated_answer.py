from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if s1 in processed:
            continue
        s1_filtered = ''.join((c.lower() for c in s1 if c.isalpha()))
        if len(s1_filtered) < 3:
            continue
        s1_counter = Counter(s1_filtered)
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            s2_filtered = ''.join((c.lower() for c in s2 if c.isalpha()))
            if len(s2_filtered) < 3:
                continue
            if s1_counter == Counter(s2_filtered):
                anagram_count += 1
                processed.add(s2)
                if anagram_count > 50:
                    return False
        processed.add(s1)
    return True