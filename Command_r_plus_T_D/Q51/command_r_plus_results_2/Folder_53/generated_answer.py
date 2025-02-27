def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize_string(lst[i])
        if len(normalized_str) < 3:
            continue
        if normalized_str in anagram_set:
            anagram_count += 1
        else:
            anagram_set.add(normalized_str)
    return anagram_count <= 8