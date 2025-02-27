def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
            if count > 18:
                return False
    return True