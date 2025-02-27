def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    eighty_nine_smallest = sorted_chars[:89]
    return sorted(eighty_nine_smallest, reverse=True)