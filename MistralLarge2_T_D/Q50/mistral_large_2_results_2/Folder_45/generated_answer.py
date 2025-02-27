from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    count = 0
    length_filtered = [s for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for s in length_filtered:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            pairs = len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            count += pairs
    return count >= 277