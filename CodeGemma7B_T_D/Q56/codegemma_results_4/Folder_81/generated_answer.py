from collections import Counter

def all_substring_of_size_n(text, n):
    substring_list = []
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if len(Counter(substring)) == n:
            substring_list.append(substring)
    return substring_list