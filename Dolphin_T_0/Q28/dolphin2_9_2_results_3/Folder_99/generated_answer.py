def return_nth_smallest_ascii(string):
    ascii_values = [ord(string[i]) for i in range(17, 66)]
    nth_smallest = sorted(ascii_values)[7]
    for i in range(17, 66):
        if ord(string[i]) == nth_smallest:
            return string[i]