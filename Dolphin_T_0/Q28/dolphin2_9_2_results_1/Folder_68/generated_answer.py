def return_nth_smallest_ascii(input_string):
    return sorted(input_string[:11], key=lambda c: ord(c))[10]