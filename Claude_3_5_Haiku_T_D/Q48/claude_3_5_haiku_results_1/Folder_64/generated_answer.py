def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[5])
    num_set = set(nums[0:6])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in num_set:
            total_sum += num
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 == 1 else hex(total_sum)[2:]