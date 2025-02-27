from functools import cmp_to_key

def return_n_greatest_chars(text):
    chars_list = list(text)
    chars_list.sort(key=cmp_to_key(lambda a, b: ord(a) - ord(b)), reverse=True)
    return chars_list[:19]