def if_contains_anagrams(strings):
    counter = 0
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            counter += len(anagrams[sorted_string])
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    return counter >= 72