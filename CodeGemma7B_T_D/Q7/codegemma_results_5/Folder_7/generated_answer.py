def all_even_ints_inclusive(nums):
    result = []
    for num in nums[661:925]:
        if num % 2 == 0:
            result.append(num)
    return result if result else []