def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    str_to_normalized = {}
    for s in lst:
        normalized = normalize_string(s)
        if len(normalized) < 3:
            continue
        if normalized in str_to_normalized:
            anagram_count += 1
        else:
            str_to_normalized[normalized] = True
    return anagram_count <= 464