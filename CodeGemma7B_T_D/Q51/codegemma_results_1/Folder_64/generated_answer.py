from collections import defaultdict

def if_contains_anagrams(str_list):
    freq_dict = defaultdict(int)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            freq_dict[sorted_word] += 1
    return len(list(filter(lambda x: x > 1, freq_dict.values()))) <= 59