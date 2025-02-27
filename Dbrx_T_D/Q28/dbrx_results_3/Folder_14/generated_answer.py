def return_nth_smallest_ascii(char_string):
    ascii_46_82 = char_string[46:83].translate(str.maketrans('', '', string.whitespace)).translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
    sorted_ascii = sorted(set([ord(c) for c in ascii_46_82]))
    return chr(sorted_ascii[15]) if len(sorted_ascii) > 15 else None