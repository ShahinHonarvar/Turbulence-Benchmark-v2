def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[7]
    excluded_set = set(nums[2:8])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in excluded_set:
            total_sum += num
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]