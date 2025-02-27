def return_nth_smallest_ascii(S):
    chars = list(S[0:11])
    ascii_vals = [ord(user) for user in chars]
    ascii_vals.sort()
    return chars[ascii_vals.index(ascii_vals[10])]