from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    for anagram_list in anagram_map.values():
        if len(anagram_list) > 1:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count >= 19