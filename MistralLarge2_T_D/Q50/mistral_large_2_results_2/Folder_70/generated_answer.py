from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_dict[norm].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 189