def all_even_ints_inclusive(nums):
    result = []
    for num in nums[6:9]:
        if num % 2 == 0:
            result.append(num)
    return result or []