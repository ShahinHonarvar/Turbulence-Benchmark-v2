from collections import Counter

def if_contains_anagrams(input_list):
    input_list = [word.lower() for word in input_list]
    counter_dict = Counter()
    for word in input_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            counter_dict[sorted_word] += 1
    return sum((val > 1 for val in counter_dict.values())) <= 206