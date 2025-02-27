def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums:
        if not num % 2:
            even_nums.append(num)
    return even_nums