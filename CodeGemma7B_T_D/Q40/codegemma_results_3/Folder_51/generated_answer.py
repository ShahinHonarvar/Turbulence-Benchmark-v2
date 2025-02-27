def return_n_smallest_chars(ch):
    ch_list = list(set(ch))
    [ch_list.pop(ch_list.index(c)) for c in set(ch) if ord(c) == min((ord(c) for c in set(ch)))]
    ch_list.sort(reverse=True)
    return ch_list[:45]