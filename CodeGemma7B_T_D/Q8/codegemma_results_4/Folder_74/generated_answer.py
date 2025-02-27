def all_even_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 == 0 and 13 <= num <= 69:
            result.append(num)
    return result