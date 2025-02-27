from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = set()
    count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        count[sorted_string] += 1
    for key in count:
        if count[key] > 1:
            anagram_pairs.add(key)
    return len(anagram_pairs) <= 464