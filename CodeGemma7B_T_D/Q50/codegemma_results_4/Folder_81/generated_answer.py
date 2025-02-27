from collections import defaultdict

def if_contains_anagrams(word_list):
    if len(word_list) < 16:
        return False
    word_dict = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_dict[sorted_word].append(word)
    for word in word_dict.values():
        if len(word) >= 16:
            return True
    return False