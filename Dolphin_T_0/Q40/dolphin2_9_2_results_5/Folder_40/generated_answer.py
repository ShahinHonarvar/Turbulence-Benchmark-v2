def return_n_smallest_chars(string):
    smallest_chars = [char for char in sorted(string)[:7]]
    smallest_chars.sort(reverse=True)
    return smallest_chars