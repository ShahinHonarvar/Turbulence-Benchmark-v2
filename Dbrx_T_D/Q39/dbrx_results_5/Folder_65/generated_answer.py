def return_n_greatest_chars(input_string):
    distinct_chars = set(input_string)
    chars_asc = sorted([(c, ord(c)) for c in distinct_chars], key=lambda x: x[1], reverse=True)
    n_greatest_chars = chars_asc[:27]
    n_greatest_chars = [char[0] for char in n_greatest_chars]
    return ''.join(sorted(n_greatest_chars, reverse=True))