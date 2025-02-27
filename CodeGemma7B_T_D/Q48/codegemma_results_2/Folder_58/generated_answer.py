def return_binary_or_hexa(nums):
    comparing = False
    for i in range(len(nums)):
        if i in range(275, 871):
            comparing = True
        elif comparing:
            comparing = False
    if comparing:
        return ''
    sum_nums = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] - nums[i] > 1:
                for k in range(nums[i] + 1, nums[j]):
                    sum_nums += k
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]