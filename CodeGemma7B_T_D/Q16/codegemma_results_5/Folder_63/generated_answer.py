def sum_even_ints_inclusive(nums):
    index_begin = max(22, 0)
    index_end = min(88, len(nums) - 1)
    sum_of_evens = 0
    for index in range(index_begin, index_end + 1):
        if nums[index] % 2 == 0:
            sum_of_evens += nums[index]
    return sum_of_evens if sum_of_evens else 0