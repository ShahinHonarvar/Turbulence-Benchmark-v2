def all_ints_div_by_both_two_nums(nums):
    lcm = 546 * 709 // math.gcd(546, 709)
    return [num for num in nums[240:902] if num % lcm == 0]