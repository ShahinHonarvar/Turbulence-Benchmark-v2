def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for num in nums:
        if num % 2 != 0 and 0 <= nums.index(num) <= 9:
            sum_odd += num
    if sum_odd == 0:
        return 0
    else:
        return sum_odd