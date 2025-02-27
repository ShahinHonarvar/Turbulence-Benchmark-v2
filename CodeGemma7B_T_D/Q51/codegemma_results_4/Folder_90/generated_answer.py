def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower().replace(' ', '')))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 0
            anagrams[sorted_string] += 1
    count = 0
    for anagram, occurrences in anagrams.items():
        if occurrences > 1:
            count += occurrences * (occurrences - 1) // 2
    return count <= 147