def return_nth_smallest_ascii(n):

    def ord_char(char):
        return ord(char)
    chars = sorted(filter(ord_char, n))[5:11]
    return chars[5] if len(chars) > 5 else None