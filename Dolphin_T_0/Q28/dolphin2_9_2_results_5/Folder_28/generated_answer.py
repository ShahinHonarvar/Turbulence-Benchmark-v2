def return_nth_smallest_ascii(s):
    vowels = sorted([s[i] for i in range(25, 78)])
    return vowels[15]