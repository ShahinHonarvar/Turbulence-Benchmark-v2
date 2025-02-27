from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            norm_str = normalize(string)
            anagram_dict[norm_str].append(string)
    anagram_pairs = 0
    for norm_str, anagrams in anagram_dict.items():
        count = len(anagrams)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 366:
                return False
    return anagram_pairs <= 366