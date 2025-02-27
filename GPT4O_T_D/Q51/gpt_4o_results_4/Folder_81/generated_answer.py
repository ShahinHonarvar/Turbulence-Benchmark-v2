from collections import defaultdict

def if_contains_anagrams(word_list):
    word_dict = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    anagram_count = 0
    for anagram_group in word_dict.values():
        n = len(anagram_group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 79:
                return False
    return True