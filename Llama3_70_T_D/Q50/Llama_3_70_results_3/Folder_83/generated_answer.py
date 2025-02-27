def if_contains_anagrams(strings):
    anagrams_count = 0
    seen = set()
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string) >= 3 and sorted_string in seen:
            anagrams_count += 1
        seen.add(sorted_string)
    return anagrams_count >= 48