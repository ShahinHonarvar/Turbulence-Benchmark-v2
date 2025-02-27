def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_string(word)
        if len(normalized_word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_count += 1
            anagram_dict[normalized_word] += 1
        else:
            anagram_dict[normalized_word] = 1
    return anagram_count <= 85