def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = 1
            else:
                anagram_dict[sorted_str] += 1
                anagram_count += anagram_dict[sorted_str]
    return anagram_count >= 61