from collections import Counter

def if_contains_anagrams(lst):
    counter_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        word_count = Counter(sorted_word)
        if any((char not in 'abcdefghijklmnopqrstuvwxyz' for char in sorted_word)):
            continue
        if sorted_word not in counter_dict:
            counter_dict[sorted_word] = 1
        else:
            counter_dict[sorted_word] += 1
    anagram_pairs = sum((count % 2 == 1 for count in counter_dict.values()))
    if anagram_pairs <= 16:
        return True
    else:
        return False