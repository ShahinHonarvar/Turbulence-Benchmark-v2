from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        count[sorted_str] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return anagram_pairs >= 35