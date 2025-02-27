import math

def find_subset_of_length_n(input_set):
    if len(input_set) < 87:
        return 0
    return math.comb(len(input_set), 87)