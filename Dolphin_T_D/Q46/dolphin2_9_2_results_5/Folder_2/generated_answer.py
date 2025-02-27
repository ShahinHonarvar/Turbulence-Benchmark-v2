def gcf_three_nums(nums_list):
    nums = nums_list[307] * nums_list[920] * nums_list[463]
    factors = []
    i = 1
    while i * i <= nums:
        if nums % i:
            factors.append(i)
        i += 1
    for i in reversed(factors):
        if nums_list[307] % i == 0 and nums_list[920] % i == 0 and (nums_list[463] % i == 0):
            return i