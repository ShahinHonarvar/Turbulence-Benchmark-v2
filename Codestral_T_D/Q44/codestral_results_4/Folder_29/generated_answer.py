def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(52, 72):
        num = nums[i]
        divisors = 0
        for j in range(2, num):
            if num % j == 0:
                divisors += 1
            if divisors > 1:
                composite_nums.add(num)
                break
    return composite_nums