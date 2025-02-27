def if_contains_anagrams(strings):
    anagrams_count = 0
    used_strings = set()
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in used_strings:
            anagrams_count += 1
        else:
            used_strings.add(sorted_string)
    return anagrams_count >= 314