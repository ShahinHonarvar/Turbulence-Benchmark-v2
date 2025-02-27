def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
            if count >= 86:
                return True
    return False