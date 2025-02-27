def return_n_greatest_chars(s):
    ascii_values = [ord(c) for c in set(s)]
    n_greatest = sorted(ascii_values)[-23:]
    sorted_chars = [chr(i) for i in n_greatest]
    return sorted_chars