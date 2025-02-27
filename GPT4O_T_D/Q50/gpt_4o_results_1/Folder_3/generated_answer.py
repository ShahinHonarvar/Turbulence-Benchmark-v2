from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_key = sorted_chars(s)
            anagram_dict[anagram_key] += 1
    count = 0
    for key in anagram_dict:
        n = anagram_dict[key]
        count += n * (n - 1) // 2
        if count >= 30:
            return True
    return False