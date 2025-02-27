from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 72