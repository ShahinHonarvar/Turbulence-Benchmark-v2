def filter_chars(a):
    chr_list = list(a)
    for i in range(22, 86):
        if chr_list[i] >= '7' and chr_list[i] <= 'e':
            chr_list[i] = None
    return ''.join([x for x in chr_list if x is not None])