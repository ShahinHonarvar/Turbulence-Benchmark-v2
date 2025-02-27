def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: x)
    n_greatest = sorted(sorted_chars, key=lambda x: ord(x), reverse=True)[:63]
    return sorted(n_greatest)