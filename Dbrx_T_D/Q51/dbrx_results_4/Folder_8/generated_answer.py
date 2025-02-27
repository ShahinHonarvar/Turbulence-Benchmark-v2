def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if string not in anagrams:
                anagrams[string] = 1
            else:
                anagrams[string] += 1
                if anagrams[string] == 68:
                    return True
    return False