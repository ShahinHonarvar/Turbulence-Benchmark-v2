def all_even_ints_exclusive(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            if 40 < num < 200:
                even_nums.append(num)
    return even_nums