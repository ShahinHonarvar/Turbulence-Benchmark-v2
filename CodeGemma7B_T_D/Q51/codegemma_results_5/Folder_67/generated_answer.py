from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted([char for char in word.lower() if char.isalpha()]))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    return len(anagram_dict) <= 5