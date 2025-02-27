def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    anagram_pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            anagram_pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_pairs >= 8