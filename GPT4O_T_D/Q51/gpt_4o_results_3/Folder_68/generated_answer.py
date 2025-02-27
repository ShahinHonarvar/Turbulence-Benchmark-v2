from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram(s):
        return len(s) >= 3 and s.isalpha()
    count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if is_valid_anagram(s_lower):
            key = ''.join(sorted(s_lower))
            anagram_dict[key].append(s_lower)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
        if count > 94:
            return False
    return True