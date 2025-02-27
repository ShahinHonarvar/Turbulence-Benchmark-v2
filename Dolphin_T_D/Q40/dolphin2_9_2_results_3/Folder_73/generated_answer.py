def return_n_smallest_chars(s):
    if len(s) < 80:
        list_chars = [i for i in s]
        list_chars.sort()
        return list_chars
    else:
        list_chars = [i for i in s]
        list_chars.sort()
        return list_chars[:80]