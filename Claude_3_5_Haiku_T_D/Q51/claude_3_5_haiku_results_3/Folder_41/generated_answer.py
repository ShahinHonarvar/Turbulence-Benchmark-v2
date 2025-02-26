def if_contains_anagrams(strings):

    def is_valid_string(s):
        return all((c.isalpha() for c in s))

    def get_sorted_lower(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3 and is_valid_string(s)]
    anagram_counts = {}
    for s in valid_strings:
        sorted_s = get_sorted_lower(s)
        anagram_counts[sorted_s] = anagram_counts.get(sorted_s, 0) + 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return total_pairs <= 52