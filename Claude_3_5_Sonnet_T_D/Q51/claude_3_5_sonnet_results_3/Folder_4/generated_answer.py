from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3:
            continue
        s1_clean = ''.join(filter(str.isalpha, s1.lower()))
        if s1_clean in processed:
            continue
        s1_counter = Counter(s1_clean)
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            if len(s2) < 3:
                continue
            s2_clean = ''.join(filter(str.isalpha, s2.lower()))
            if s2_clean in processed:
                continue
            if len(s1_clean) == len(s2_clean) and s1_counter == Counter(s2_clean):
                anagram_count += 1
                processed.add(s1_clean)
                processed.add(s2_clean)
                if anagram_count > 84:
                    return False
                break
    return True