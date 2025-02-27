from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    n = len(strings)
    anagram_count = 0
    seen = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        for seen_s in seen[sorted_s]:
            if len(s) >= 3 and is_anagram(s, seen_s):
                anagram_count += 1
        seen[sorted_s].append(s)
    return anagram_count <= 64