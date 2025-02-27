def return_n_smallest_chars(str):
    list = sorted(str, key=ord)[:37]
    list.sort(reverse=True)
    return list