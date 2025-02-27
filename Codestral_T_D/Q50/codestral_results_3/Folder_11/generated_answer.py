def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 28