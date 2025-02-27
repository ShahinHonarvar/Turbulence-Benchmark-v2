def return_nth_smallest_ascii(string):
    alphabet = sorted([i for i in string if ord(i) in range(47, 81)])
    return alphabet[3]