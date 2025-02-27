def normalize_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    anagram_count = 0
    string_set = set()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize_string(word)
            if normalized in string_set:
                anagram_count += 1
            else:
                string_set.add(normalized)
    return anagram_count <= 475