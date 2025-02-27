def if_contains_anagrams(strings):
    anagrams_count = 0
    sorted_strings = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.casefold()))
        if sorted_string in sorted_strings:
            anagrams_count += len(sorted_strings[sorted_string])
            sorted_strings[sorted_string].append(string)
        else:
            sorted_strings[sorted_string] = [string]
    return anagrams_count >= 155