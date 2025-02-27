from functools import cmp_to_key

def return_n_greatest_chars(text):
    sorted_list = sorted(text, key=cmp_to_key(lambda x, y: ord(x) - ord(y)))
    return sorted_list[-76:]