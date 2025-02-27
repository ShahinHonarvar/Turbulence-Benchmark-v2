def return_nth_smallest_ascii(string):
    string = string[35:53]
    return sorted(string, key=lambda x: ord(x))[9]