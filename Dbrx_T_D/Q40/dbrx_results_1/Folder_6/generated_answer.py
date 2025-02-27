def return_n_smallest_chars(string):
    linen = [char for char in string if ord(char) < 100]
    linen.sort(key=ord, reverse=False)
    return linen[:47]