def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 277