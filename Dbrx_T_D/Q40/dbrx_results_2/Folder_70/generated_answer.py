import numpy as np

def return_n_smallest_chars(string):
    chars = np.array(list(string))
    sorted_chars = np.sort(chars.view(np.uint8))
    smallest_chars = sorted_chars[:2]
    return smallest_chars[::-1].tolist()