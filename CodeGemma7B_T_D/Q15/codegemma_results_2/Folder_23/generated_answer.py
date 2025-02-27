def sum_odd_ints_inclusive(nums):
    initial_index = 52
    final_index = 71
    current_index = 0
    sum = 0
    while current_index <= final_index:
        if current_index >= initial_index and nums[current_index] % 2 != 0:
            sum += nums[current_index]
        current_index += 1
    return sum