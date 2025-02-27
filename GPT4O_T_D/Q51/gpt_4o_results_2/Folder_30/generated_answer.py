from collections import defaultdict

def if_contains_anagrams(word_list):
    word_list = [word.lower() for word in word_list if len(word) >= 3]
    anagram_dict = defaultdict(int)
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] += 1
    pair_count = 0
    for count in anagram_dict.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
        if pair_count > 28:
            return False
    return True