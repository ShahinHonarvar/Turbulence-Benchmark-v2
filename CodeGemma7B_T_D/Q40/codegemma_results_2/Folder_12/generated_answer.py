def return_n_smallest_chars(str_chars):
    n = 61
    if len(str_chars) >= n:
        return sorted(str_chars[:n], reverse=True)
    else:
        lst_chars = sorted(str_chars, reverse=True)
        num_missing = n - len(lst_chars)
        for i in range(num_missing):
            lst_chars.append(lst_chars[-1])
    return lst_chars