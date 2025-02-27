def all_even_ints_inclusive(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            if 0 <= nums.index(num) <= 6:
                result.append(num)
    if len(result) == 0:
        return []
    else:
        return result