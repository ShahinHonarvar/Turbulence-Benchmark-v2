from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    for group in anagram_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 91