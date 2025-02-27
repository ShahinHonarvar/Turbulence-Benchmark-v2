def if_contains_anagrams(strings):
    anagrams_count = 0
    seen = {}
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3:
            continue
        for char in string_lower:
            if not char.isalpha():
                break
        else:
            if sorted_string in seen:
                seen[sorted_string] += 1
                anagrams_count += seen[sorted_string]
            else:
                seen[sorted_string] = 1
    return anagrams_count <= 57