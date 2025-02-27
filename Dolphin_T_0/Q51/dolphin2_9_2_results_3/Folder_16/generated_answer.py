from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(s):
        return Counter(s.lower())

    def is_anagram(s1, s2):
        return count_anagrams(s1) == count_anagrams(s2)

    def find_anagram_pairs(lst):
        pairs = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    pairs.append((lst[i], lst[j]))
        return pairs
    anagram_pairs = find_anagram_pairs([s for s in lst if len(s) >= 3])
    return len(anagram_pairs) <= 24