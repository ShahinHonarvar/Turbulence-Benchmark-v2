from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = sorted_string(word)
            anagram_dict[sorted_word] += 1
    for occurrences in anagram_dict.values():
        if occurrences > 1:
            count += occurrences * (occurrences - 1) // 2
            if count >= 38:
                return True
    return False