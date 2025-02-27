def if_contains_anagrams(lst):
    anagrams_count = 0
    sorted_strings = {}
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in sorted_strings:
            anagrams_count += len(sorted_strings[sorted_string])
            sorted_strings[sorted_string].append(string)
        else:
            sorted_strings[sorted_string] = [string]
    return anagrams_count >= 64