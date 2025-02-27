def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower(), key=str.casefold))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = 0
    for anagram in anagrams.values():
        if anagram >= 3:
            count += anagram * (anagram - 1) // 2
    return count >= 72