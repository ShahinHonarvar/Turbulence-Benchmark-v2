from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    seen = set()
    for s in string_list:
        s = ''.join(filter(str.isalpha, s.lower()))
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            anagram_count += 1
            if anagram_count > 67:
                return False
        else:
            seen.add(sorted_s)
    return True