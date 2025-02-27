def return_nth_smallest_ascii(val):
    restr = val[1:37]
    freq = [0] * 128
    for i in restr:
        freq[ord(i)] += 1
    count = 0
    for i in range(128):
        count += freq[i]
        if count == 15:
            return chr(i)