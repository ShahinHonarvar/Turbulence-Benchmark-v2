def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    sum = 0
    for i in range(25, 60):
        if i in nums and i % 2 == 0:
            sum += i
    return sum