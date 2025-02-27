def find_subset_of_length_n(set_of_element):
    n = 72
    length_ = len(set_of_element)
    if length_ < n:
        return 0
    if length_ == n:
        return 2 ** n - 1
    return 2 ** length_ - 1 - (2 ** (length_ - n) - 1)