def return_n_smallest_chars(s):
    s = [char for char in s]
    s.sort()
    smallest_ascii = s[:61]
    smallest_ascii.sort(reverse=True)
    return smallest_ascii