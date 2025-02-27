from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_count[sorted_str(word)] += 1
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs >= 41:
                return True
    return False