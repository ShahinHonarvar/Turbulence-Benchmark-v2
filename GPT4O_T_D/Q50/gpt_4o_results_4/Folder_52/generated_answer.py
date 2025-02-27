from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    count = 0
    for count_val in anagram_dict.values():
        if count_val > 1:
            count += count_val * (count_val - 1) // 2
        if count >= 58:
            return True
    return False