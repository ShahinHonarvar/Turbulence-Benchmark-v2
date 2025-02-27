from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams_dict[sorted_word] += 1
    for count_value in anagrams_dict.values():
        if count_value > 1:
            count += count_value * (count_value - 1) // 2
            if count >= 60:
                return True
    return False