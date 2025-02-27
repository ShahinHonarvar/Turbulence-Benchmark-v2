def palindrome_of_length_n(in_string):
    in_string = in_string.lower()
    out_set = set()
    for i in range(len(in_string) - 32):
        if in_string[i:i + 33] == in_string[i:i + 33][::-1]:
            out_set.add(in_string[i:i + 33])
    return out_set