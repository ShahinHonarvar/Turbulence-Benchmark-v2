def return_n_smallest_chars(s):
    result = [char for char in s]
    result.sort(key=lambda x: x, reverse=True)
    return result[:49]