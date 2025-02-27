from functools import cmp_to_key

def return_n_greatest_chars(string):
    list_of_chars = list(string)
    list_of_chars.sort(key=cmp_to_key(lambda char_a, char_b: ord(char_b) - ord(char_a)), reverse=True)
    return list_of_chars[:20]