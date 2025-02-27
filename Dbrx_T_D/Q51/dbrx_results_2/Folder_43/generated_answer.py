def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(string.lower())).rstrip('023456789')
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    return len(set(anagrams)) <= 3