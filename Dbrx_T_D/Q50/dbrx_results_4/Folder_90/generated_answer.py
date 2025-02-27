def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    total_anagrams = 0
    for count in anagrams.values():
        total_anagrams += count * (count - 1) // 2
    return total_anagrams >= 177