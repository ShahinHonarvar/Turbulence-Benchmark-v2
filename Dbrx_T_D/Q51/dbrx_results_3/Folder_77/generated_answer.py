def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagrams:
            anagrams[sorted_string] = 0
        anagrams[sorted_string] += 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams <= 17