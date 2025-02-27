def return_binary_or_hexa(nums):
    right_interval = nums[78] - nums[44] - 1
    miss_cnt = 45 - len(nums)
    if miss_cnt >= right_interval:
        return ''
    sum = 0
    cache = set(nums)
    for i in range(nums[44] + 1, nums[78] + 1):
        if i not in cache:
            sum += i
    if sum & 1:
        result = bin(sum)[2:]
    else:
        result = hex(sum)[2:]
    return result