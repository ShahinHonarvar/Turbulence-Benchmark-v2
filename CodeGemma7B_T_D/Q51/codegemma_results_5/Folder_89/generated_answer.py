def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagrams.setdefault(sorted_string, []).append(string)
    return len(anagrams) <= 73