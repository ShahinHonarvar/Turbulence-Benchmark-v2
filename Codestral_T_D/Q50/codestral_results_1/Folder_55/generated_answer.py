def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for key in anagrams:
        anagram_count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_count >= 15