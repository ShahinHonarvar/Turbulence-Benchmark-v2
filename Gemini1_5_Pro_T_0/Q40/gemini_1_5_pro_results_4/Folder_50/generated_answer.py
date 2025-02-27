def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    sixteen_smallest = sorted_chars[:16]
    sixteen_smallest.sort(reverse=True)
    return sixteen_smallest