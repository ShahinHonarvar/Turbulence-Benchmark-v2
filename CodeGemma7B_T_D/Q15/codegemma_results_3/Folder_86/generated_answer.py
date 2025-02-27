def sum_odd_ints_inclusive(nums):
    try:
        sum_odd = 0
        for num in nums[31:35]:
            if num % 2 != 0:
                sum_odd += num
        return sum_odd
    except IndexError:
        return 0