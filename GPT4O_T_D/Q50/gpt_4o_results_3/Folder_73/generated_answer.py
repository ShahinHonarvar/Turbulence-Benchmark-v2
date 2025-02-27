from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_map[sorted_string] += 1
    for count_of_anagrams in anagram_map.values():
        if count_of_anagrams > 1:
            count += count_of_anagrams * (count_of_anagrams - 1) // 2
            if count >= 91:
                return True
    return False