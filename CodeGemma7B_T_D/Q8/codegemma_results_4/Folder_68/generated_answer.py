def all_even_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            if num < 8:
                result.append(num)
    return result