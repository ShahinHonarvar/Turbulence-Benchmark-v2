from collections import defaultdict

def if_contains_anagrams(str_lst):
    anagram_counts = defaultdict(int)
    for word in str_lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word] += 1
        if anagram_counts[sorted_word] > 147:
            return False
    return True