def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    thirteen_smallest = sorted_chars[:13]
    thirteen_smallest.sort(reverse=True)
    return thirteen_smallest