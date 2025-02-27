def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [string]
        else:
            anagrams[sorted_string].append(string)
    for group in anagrams.values():
        if len(group) > 57:
            return False
    return True