def return_n_greatest_chars(arr):
    norepeat = list(set(arr))
    norepeat.sort(key=ord, reverse=True)
    return norepeat[:43]