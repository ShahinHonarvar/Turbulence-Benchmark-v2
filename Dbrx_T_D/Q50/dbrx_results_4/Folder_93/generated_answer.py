def if_contains_anagrams(strings):
    anagrams_count = 0
    used_strings = set()
    for string in strings:
        if len(string) < 3 or string.lower() in used_strings:
            continue
        used_strings.add(string.lower())
        sorted_string = ''.join(sorted(string.lower()))
        for other_string in strings:
            if len(other_string) >= 3 and other_string.lower() != string.lower() and (''.join(sorted(other_string.lower())) == sorted_string):
                anagrams_count += 1
                used_strings.add(other_string.lower())
    return anagrams_count >= 18