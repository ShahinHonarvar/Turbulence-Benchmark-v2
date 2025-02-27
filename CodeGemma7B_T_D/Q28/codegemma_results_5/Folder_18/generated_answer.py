def return_nth_smallest_ascii(str):
    five_smallest = sorted([ord(Char) for Char in str[51:61] if ord(Char) > 127])[0]
    return chr(five_smallest)