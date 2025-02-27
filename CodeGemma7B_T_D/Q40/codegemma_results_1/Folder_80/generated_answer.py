from functools import cmp_to_key

def return_n_smallest_chars(text):
    ordered_text = sorted(text, key=cmp_to_key(lambda c1, c2: ord(c1) - ord(c2)))
    return ordered_text[:35]