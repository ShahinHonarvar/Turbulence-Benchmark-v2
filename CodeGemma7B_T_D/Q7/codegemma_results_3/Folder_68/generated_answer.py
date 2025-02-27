def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0 and 0 <= num <= 8:
            even_nums.append(num)
    return even_nums