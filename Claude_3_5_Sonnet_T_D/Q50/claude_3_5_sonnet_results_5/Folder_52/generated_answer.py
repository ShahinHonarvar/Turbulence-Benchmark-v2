from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs >= 58