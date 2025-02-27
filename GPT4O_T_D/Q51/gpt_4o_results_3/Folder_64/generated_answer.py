from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s))
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    anagram_count = defaultdict(int)
    for s in normalized_strings:
        if len(s) >= 3:
            anagram_count[sorted_str(s)] += 1
    pair_count = 0
    for count in anagram_count.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count > 59:
                return False
    return pair_count <= 59