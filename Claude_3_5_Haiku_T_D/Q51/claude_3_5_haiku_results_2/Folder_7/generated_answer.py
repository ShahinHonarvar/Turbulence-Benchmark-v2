def if_contains_anagrams(strings):

    def is_valid_string(s):
        return len(s) >= 3 and s.isalpha()

    def get_sorted_key(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    seen_keys = {}
    for s in strings:
        if not is_valid_string(s):
            continue
        key = get_sorted_key(s)
        if key in seen_keys:
            anagram_pairs += seen_keys[key]
            seen_keys[key] += 1
        else:
            seen_keys[key] = 1
        if anagram_pairs > 445:
            return False
    return True