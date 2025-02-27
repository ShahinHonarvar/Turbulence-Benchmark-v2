def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))
    eighty_seven_chars = sorted_chars[:87]
    eighty_seven_chars.reverse()
    return eighty_seven_chars