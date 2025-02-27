from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    count = 0
    for count_value in anagram_dict.values():
        if count_value > 1:
            count += count_value * (count_value - 1) // 2
            if count >= 25:
                return True
    return False