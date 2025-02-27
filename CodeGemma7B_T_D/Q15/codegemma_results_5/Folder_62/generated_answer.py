def sum_odd_ints_inclusive(num_list):
    """ Function to calculate the sum of odd integers from index 91 to index 99, inclusive. """
    odd_sum = 0
    for i in range(91, 99 + 1):
        if i % 2 != 0:
            odd_sum += num_list[i]
    return odd_sum or 0