def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_chars = ''.join(sorted(string.lower()))
        if sorted_chars in anagram_dict:
            anagram_dict[sorted_chars] += 1
        else:
            anagram_dict[sorted_chars] = 1
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 131