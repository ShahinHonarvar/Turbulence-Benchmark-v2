from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_key = sorted_str(word)
            anagram_dict[anagram_key].append(word)
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 407:
                return False
    return count <= 407