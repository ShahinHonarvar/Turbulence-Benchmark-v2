def sum_even_ints_inclusive(nums):
    count = 0
    sum = 0
    for i in range(68, 87):
        num = nums[i]
        if num % 2 == 0:
            count += 1
            sum += num
    return sum if count else 0