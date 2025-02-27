def sum_even_ints_inclusive(nums):
    sum_of_evens = 0
    for num in nums[4:9]:
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens or 0