def composite_nums_between_indices(nums):
    result = set()
    for num in nums[22:89]:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                result.add(num)
                break
    return result