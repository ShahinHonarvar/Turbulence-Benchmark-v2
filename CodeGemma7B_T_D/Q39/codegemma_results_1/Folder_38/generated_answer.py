from functools import cmp_to_key

def return_n_greatest_chars(text):
    sorted_text = sorted(text, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=True)
    return sorted_text[:45]