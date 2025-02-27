def if_contains_anagrams(strings):
    anagrams_count = 0
    unique_strings = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in unique_strings:
            anagrams_count += 1
        else:
            unique_strings.add(sorted_string)
    return anagrams_count >= 411