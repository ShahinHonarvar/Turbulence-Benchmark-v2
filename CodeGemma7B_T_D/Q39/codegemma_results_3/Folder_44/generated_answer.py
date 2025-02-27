def return_n_greatest_chars(s):
    check = len(s)
    if len(s) == 73:
        return sorted(s)
    else:
        while len(s) != 73:
            i = max(s)
            s.remove(i)
        return sorted(s)