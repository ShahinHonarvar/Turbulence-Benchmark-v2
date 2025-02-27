def return_nth_smallest_ascii(string):
    return min((c for c in string[21:60] if ord(c) > ord('a')))