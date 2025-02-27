def return_n_greatest_chars(s):
    sorted_string = sorted(s, key=lambda c: ord(c), reverse=True)[:66]
    sorted_string.sort()
    return sorted_string