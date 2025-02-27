def return_nth_smallest_ascii(s):
    asciis = [ord(c) for c in s[4:34] if c not in ' ,.!?:;-']
    return chr(sorted(asciis)[3])