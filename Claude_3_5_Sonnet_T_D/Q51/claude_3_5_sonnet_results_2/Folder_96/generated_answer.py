from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, s1 in enumerate(string_list):
        if len(s1) < 3 or s1.lower() in processed:
            continue
        s1_letters = ''.join(filter(str.isalpha, s1.lower()))
        s1_counter = Counter(s1_letters)
        for s2 in string_list[i + 1:]:
            if len(s2) < 3:
                continue
            s2_letters = ''.join(filter(str.isalpha, s2.lower()))
            if len(s1_letters) == len(s2_letters) and Counter(s2_letters) == s1_counter:
                anagram_count += 1
                processed.add(s1.lower())
                processed.add(s2.lower())
                break
        if anagram_count > 2:
            return False
    return True