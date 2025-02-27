from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in checked_pairs:
                    anagram_count += 1
                    checked_pairs.add(pair)
    return anagram_count <= 91