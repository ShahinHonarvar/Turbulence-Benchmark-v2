from collections import Counter

def if_contains_anagrams(str_list):
    str_Counter = Counter((str.lower() for str in str_list))
    pairs = 0
    for str in str_list:
        if len(str) >= 3:
            pairs += str_Counter[str[::-1]]
    return pairs >= 92