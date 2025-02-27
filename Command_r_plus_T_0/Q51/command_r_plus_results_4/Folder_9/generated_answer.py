def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    string_set = set()
    for word in lst:
        normalized_word = normalize_string(word)
        if len(normalized_word) < 3:
            continue
        if normalized_word in string_set:
            anagram_count += 1
        else:
            string_set.add(normalized_word)
    return anagram_count <= 475