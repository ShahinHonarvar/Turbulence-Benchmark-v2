def return_nth_smallest_ascii(str):
    mask = set(str)
    ch_list = [ch for ch in mask if str.index(ch) in range(3, 27)]
    ch_list.sort(key=lambda ch: ord(ch))
    return ch_list[4]