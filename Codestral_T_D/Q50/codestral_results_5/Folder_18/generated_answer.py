def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            count += anagrams[sorted_string]
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return count >= 10 ** 6