def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = 1
        else:
            count += anagrams[sorted_string]
            anagrams[sorted_string] += 1
    return count >= 73