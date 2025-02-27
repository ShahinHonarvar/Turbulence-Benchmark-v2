def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_map:
                anagram_map[sorted_string] += 1
            else:
                anagram_map[sorted_string] = 1
    for count in anagram_map.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 9