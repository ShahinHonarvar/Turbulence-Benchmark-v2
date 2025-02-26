def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[4])
    present = set(nums[0:5])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present:
            total_sum += num
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]