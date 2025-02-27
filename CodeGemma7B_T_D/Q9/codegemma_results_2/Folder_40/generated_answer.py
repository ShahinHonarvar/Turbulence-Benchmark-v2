def all_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0 and 0 <= num <= 2:
            odd_nums.append(num)
    return odd_nums