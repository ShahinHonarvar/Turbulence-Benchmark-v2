from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 69:
                return False
    return True