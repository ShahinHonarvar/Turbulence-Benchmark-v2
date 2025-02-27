def return_n_greatest_chars(s):
    result = sorted([c for c in s], key=lambda x: -ord(x))
    return result[:79]