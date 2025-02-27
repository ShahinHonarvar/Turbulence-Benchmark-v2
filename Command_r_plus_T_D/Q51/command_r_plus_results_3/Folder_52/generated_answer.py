def normalize_string(s):
    return ''.join((c.lower() for c in s if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    normalized_strings = [normalize_string(s) for s in lst]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j] and len(normalized_strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 43:
                    return False
    return True