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
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            s2_lower = ''.join(filter(str.isalpha, s2.lower()))
            if len(s2_lower) < 3:
                continue
            if s1_counter == Counter(s2_lower):
                anagram_count += 1
                processed.add(s2)
                if anagram_count > 79:
                    return False
        processed.add(s1)
    return True