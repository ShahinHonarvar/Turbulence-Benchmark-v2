def if_contains_anagrams(strings):
    anagrams_count = 0
    used_strings = set()
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in used_strings:
            continue
        used_strings.add(sorted_string)
        anagrams_count += strings.count(string)
    return anagrams_count >= 97