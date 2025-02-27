def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) < 3:
            continue
        if string not in anagrams:
            anagrams[string] = []
        anagrams[string].append(string)
    for group in anagrams.values():
        if len(group) >= 8:
            return True
    return False