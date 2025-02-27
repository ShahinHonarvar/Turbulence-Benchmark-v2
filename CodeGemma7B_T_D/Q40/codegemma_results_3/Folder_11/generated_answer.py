def return_n_smallest_chars(chars):
    list = []
    for i in chars:
        list.append(ord(i))
    list.sort()
    return chars[0:17]