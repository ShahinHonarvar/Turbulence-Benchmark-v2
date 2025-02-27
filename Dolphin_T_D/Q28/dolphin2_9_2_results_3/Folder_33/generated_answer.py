def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(22, 75)]
    asciis = [ord(c) for c in chars]
    nth_smallest = sorted(asciis)[11]
    for c in chars:
        if ord(c) == nth_smallest:
            return c