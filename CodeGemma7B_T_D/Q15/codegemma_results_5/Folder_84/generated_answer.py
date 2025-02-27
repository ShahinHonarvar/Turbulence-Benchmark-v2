def sum_odd_ints_inclusive(num_list):
    """
    Write a function called 'sum_odd_ints_inclusive' that takes one argument,
    a list of integers, and returns the sum of all odd integers from
    index 43 to index 86, both inclusive. If no odd integers exist in the
    specified range, the function should return 0.
    """
    sum_odd_nums = 0
    for idx in range(43, 87):
        if idx < len(num_list) and num_list[idx] % 2 != 0:
            sum_odd_nums += num_list[idx]
    return sum_odd_nums if sum_odd_nums > 0 else 0