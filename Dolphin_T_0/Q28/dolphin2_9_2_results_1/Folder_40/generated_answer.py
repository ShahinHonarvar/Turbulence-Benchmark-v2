def return_nth_smallest_ascii(s):
    asciis = [ord(s[i]) for i in range(len(s)) if i < 5]
    return chr(sorted(asciis)[4])