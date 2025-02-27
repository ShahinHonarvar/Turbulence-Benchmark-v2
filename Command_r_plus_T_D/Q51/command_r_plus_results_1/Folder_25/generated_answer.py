def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    normalized_strings = [normalize_string(s) for s in lst]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if len(normalized_strings[i]) >= 3 and len(normalized_strings[j]) >= 3:
                if sorted(normalized_strings[i]) == sorted(normalized_strings[j]):
                    anagram_count += 1
                    if anagram_count > 67:
                        return False
    return True