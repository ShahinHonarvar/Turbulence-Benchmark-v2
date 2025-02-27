from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_dict[norm] += 1
    for k in anagram_dict:
        n = anagram_dict[k]
        if n > 1:
            count += n * (n - 1) // 2
            if count > 188:
                return False
    return True