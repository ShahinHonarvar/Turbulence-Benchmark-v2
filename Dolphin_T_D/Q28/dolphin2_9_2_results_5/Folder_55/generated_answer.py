def return_nth_smallest_ascii(s):
    subs = [''.join(sorted(s[i:i + 13])) for i in range(len(s) - 12)]
    return subs[0][12]