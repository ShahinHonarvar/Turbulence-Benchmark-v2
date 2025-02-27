def sum_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums[23:24]:
        if num % 2 != 0:
            odd_nums.append(num)
    return sum(odd_nums) if odd_nums else 0