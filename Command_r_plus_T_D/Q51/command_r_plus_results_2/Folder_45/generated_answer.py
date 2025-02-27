def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    string_set = set()
    for word in lst:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in string_set:
            anagram_count += 1
        else:
            string_set.add(normalized_word)
    return anagram_count <= 464