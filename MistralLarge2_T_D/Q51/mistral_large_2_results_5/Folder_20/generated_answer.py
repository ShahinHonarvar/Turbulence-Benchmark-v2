from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(strings):
        anagram_count = 0
        checked_pairs = set()
        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                if (i, j) in checked_pairs or (j, i) in checked_pairs:
                    continue
                if len(strings[i]) < 3 or len(strings[j]) < 3:
                    continue
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    checked_pairs.add((j, i))
        return anagram_count
    return count_anagram_pairs(strings) <= 131