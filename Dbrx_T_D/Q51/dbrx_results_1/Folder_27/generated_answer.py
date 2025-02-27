import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if string in anagrams:
                anagrams[string] += 1
                if anagrams[string] > 1 and (string, anagrams[string]) not in itertools.combinations_with_replacement(anagrams.keys(), 2):
                    if len([(k, v) for k, v in anagrams.items() if v > 1]) > 113:
                        return True
            else:
                anagrams[string] = 1
    return False