from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    pairs = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted(s.lower())
            pairs[tuple(sorted_s)].append(s)
    count = 0
    for key in pairs:
        if len(pairs[key]) > 1:
            count += len(pairs[key]) - 1
    return count <= 81