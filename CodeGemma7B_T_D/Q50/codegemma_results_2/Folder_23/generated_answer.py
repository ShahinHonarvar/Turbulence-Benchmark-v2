from itertools import combinations_with_replacement 

def if_contains_anagrams(word_list):
    letter_combinations = combinations_with_replacement('abcdefghijklmnopqrstuvwxyz', 3)
    swapped_letter_combinations = []
    for combination in letter_combinations:
        swapped = ''.join(combination)
        swapped_letter_combinations.append(swapped)
    swapped_word_list = [word.lower() for word in word_list if len(word) >= 3]
    zipped_lists = list(zip(swapped_word_list, swapped_letter_combinations))
    swapped_anagrams = [word for anagram, word in zipped_lists if anagram in zipped_lists]
    if len(swapped_anagrams) >= 67:
        return True
    return False