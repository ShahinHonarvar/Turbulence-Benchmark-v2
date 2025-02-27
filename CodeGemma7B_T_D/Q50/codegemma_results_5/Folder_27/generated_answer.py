def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    count = 0
    for anagram_count in anagrams.values():
        if anagram_count >= 3:
            count += anagram_count * (anagram_count - 1) // 2
    return count >= 86