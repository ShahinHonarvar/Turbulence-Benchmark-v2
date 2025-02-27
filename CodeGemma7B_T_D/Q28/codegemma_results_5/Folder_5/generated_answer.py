def return_nth_smallest_ascii(str):
    str = str[5:89]
    return str[sorted(range(len(str)), key=str.__getitem__).index(12)]