from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    for key in anagram_dict:
        anagram_list = anagram_dict[key]
        if len(anagram_list) > 1:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count >= 411