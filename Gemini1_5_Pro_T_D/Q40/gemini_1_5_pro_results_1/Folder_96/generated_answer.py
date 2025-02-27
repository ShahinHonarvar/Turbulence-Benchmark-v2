def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    twenty_smallest_chars = sorted_chars[:20]
    twenty_smallest_chars.sort(reverse=True)
    return twenty_smallest_chars