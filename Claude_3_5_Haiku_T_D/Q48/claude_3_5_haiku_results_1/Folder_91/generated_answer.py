def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[6])
    subset = set(nums[0:7])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in subset:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]