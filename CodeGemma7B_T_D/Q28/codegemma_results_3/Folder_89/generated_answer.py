def return_nth_smallest_ascii(string):
    for char in sorted(string[24:72]):
        if len(set(char)) == len(char):
            return char