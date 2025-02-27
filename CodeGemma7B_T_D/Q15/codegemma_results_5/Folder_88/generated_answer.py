def sum_odd_ints_inclusive(list_of_nums):
    """Sums all odd integers from index 4 to 8, inclusive."""
    sum_of_odd_nums = 0
    for num in range(4, 9):
        if num % 2 != 0:
            sum_of_odd_nums += num
    return sum_of_odd_nums if sum_of_odd_nums else 0