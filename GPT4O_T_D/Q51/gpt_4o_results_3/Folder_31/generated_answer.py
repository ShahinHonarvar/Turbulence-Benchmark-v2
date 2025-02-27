from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 65