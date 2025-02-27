def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = 0
        anagram_dict[sorted_string] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 153:
            return True
    return False