def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for anagram in anagrams.values():
        count += len(anagram) * (len(anagram) - 1) // 2
    return count >= 96