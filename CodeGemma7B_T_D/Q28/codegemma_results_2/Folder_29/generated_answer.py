from functools import cmp_to_key

def return_nth_smallest_ascii(text):
    return sorted(text[5:11], key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[5]