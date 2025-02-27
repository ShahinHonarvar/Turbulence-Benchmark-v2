from itertools import product

def all_substring_of_size_n(str):
    unique_substr = set()
    for i in range(len(str) - 43):
        if len(set(str[i:i + 45])) == 45:
            unique_substr.add(str[i:i + 45])
    return list(unique_substr)