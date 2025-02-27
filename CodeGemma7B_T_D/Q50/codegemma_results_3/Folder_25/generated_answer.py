from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    word_dict = defaultdict(list)
    for word in list_of_strings:
        clean_word = ''.join(sorted(word.lower()))
        if len(clean_word) >= 3:
            word_dict[clean_word].append(word)
    count_anagrams = 0
    for group in word_dict.values():
        if len(group) >= 14:
            count_anagrams += len(group) // 2
    return count_anagrams >= 14