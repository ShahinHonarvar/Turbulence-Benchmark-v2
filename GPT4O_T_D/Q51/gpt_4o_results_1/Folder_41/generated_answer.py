from collections import defaultdict

def if_contains_anagrams(strings):

    def signature(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))

    def is_anagram_pair(s1, s2):
        return signature(s1) == signature(s2) and len(s1) >= 3 and (len(s2) >= 3)
    n = len(strings)
    pair_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram_pair(strings[i], strings[j]):
                pair_count += 1
                if pair_count > 52:
                    return False
    return True