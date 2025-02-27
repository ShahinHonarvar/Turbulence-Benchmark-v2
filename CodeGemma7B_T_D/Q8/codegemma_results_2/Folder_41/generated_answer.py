def all_even_ints_exclusive(nums):
    filtered_nums = []
    for num in nums:
        if num % 2 == 0 and num not in range(9, 10):
            filtered_nums.append(num)
    return filtered_nums