from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if s1 in processed:
            continue
        s1 = ''.join(filter(str.isalpha, s1.lower()))
        if len(s1) < 3:
            continue
        s1_counter = Counter(s1)
        for j, s2 in enumerate(string_list[i + 1:], start=i + 1):
            s2 = ''.join(filter(str.isalpha, s2.lower()))
            if len(s2) < 3:
                continue
            if len(s1) == len(s2) and s1_counter == Counter(s2):
                anagram_count += 1
                processed.add(string_list[j])
                if anagram_count > 88:
                    return False
        processed.add(string_list[i])
    return True