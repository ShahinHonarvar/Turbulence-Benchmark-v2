from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count_pairs = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return count_pairs <= 61