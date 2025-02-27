def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    count = 0
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 21