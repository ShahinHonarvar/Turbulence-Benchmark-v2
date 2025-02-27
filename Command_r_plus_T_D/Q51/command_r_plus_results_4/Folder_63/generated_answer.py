def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    string_set = set()
    for string in lst:
        if len(string) < 3:
            continue
        normalized = normalize_string(string)
        if normalized in string_set:
            anagram_count += 1
        else:
            string_set.add(normalized)
    return anagram_count <= 423