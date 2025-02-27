from collections import Counter

def if_contains_anagrams(str_list):
    letters_dict = Counter(''.join(str_list))
    pairs_count = 0
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in letters_dict:
            pairs_count += letters_dict[sorted_word]
            letters_dict[sorted_word] -= 1
    return pairs_count >= 276