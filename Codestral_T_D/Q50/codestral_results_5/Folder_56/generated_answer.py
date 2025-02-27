def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
            count += len(anagrams[sorted_string]) - 1
        else:
            anagrams[sorted_string] = [string]
    return count >= 77