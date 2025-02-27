def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    str_set = set()
    for s in lst:
        normalized_s = normalize_string(s)
        if len(normalized_s) < 3:
            continue
        if normalized_s in str_set:
            anagram_count += 1
        else:
            str_set.add(normalized_s)
    return anagram_count <= 401