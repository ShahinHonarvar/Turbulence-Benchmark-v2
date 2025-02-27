from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 401:
                return False
    return True