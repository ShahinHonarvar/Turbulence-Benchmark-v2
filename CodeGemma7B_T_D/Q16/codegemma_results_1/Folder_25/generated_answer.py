def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(29, 95):
        if i >= len(nums):
            continue
        num = nums[i]
        if num % 2 == 0:
            result += num
    return result if result else 0