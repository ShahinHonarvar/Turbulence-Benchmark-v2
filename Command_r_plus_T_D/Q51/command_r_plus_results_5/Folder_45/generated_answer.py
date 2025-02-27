def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    string_set = set()
    for s in lst:
        normalized = normalize_string(s)
        if len(normalized) < 3:
            continue
        if normalized in string_set:
            anagram_count += 1
        else:
            string_set.add(normalized)
    return anagram_count <= 464