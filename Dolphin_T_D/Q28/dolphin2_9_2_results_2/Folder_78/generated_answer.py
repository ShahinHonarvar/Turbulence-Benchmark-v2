def return_nth_smallest_ascii(string):
    return chr(sorted([ord(c) for c in string[:88]])[13])