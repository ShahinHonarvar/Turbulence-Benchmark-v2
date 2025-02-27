def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return [sorted_chars[i] for i in range(48)]