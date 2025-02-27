from collections import Counter

def all_substring_of_size_n(str):
    substring = []
    for i in range(len(str) - 31):
        substring.append(str[i:i + 32])
    return list(set(substring))