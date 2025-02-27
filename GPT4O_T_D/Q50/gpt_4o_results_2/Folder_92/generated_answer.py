from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += value // 2
        if count >= 2:
            return True
    return False