from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word))
        anagram_pairs[key].append(word)
    count = sum((len(words) * (len(words) - 1) // 2 for words in anagram_pairs.values() if len(words) > 1))
    return count >= 8