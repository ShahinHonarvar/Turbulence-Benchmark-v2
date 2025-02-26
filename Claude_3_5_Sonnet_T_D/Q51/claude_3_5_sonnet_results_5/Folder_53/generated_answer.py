from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if s1 in processed:
            continue
        s1_clean = ''.join(filter(str.isalpha, s1.lower()))
        if len(s1_clean) < 3:
            continue
        s1_counter = Counter(s1_clean)
        for s2 in string_list[i + 1:]:
            s2_clean = ''.join(filter(str.isalpha, s2.lower()))
            if len(s2_clean) < 3:
                continue
            if s1_counter == Counter(s2_clean):
                anagram_count += 1
                processed.add(s2)
                if anagram_count > 8:
                    return False
                break
        processed.add(s1)
    return True