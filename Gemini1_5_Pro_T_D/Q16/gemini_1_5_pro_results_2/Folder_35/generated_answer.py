def sum_even_ints_inclusive(nums):
    sum_of_evens = 0
    for i in range(30, 49):
        if i in range(len(nums)):
            if nums[i] % 2 == 0:
                sum_of_evens += nums[i]
    return sum_of_evens