def return_n_smallest_chars(s):
    smallest_chars = [char for char in s if ord(char) <= int(max([ord(c) for c in s])) - int(min([ord(c) for c in s])) + 37]
    return sorted(smallest_chars, reverse=True)