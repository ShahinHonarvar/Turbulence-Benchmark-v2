def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[10])
    num_set = set(nums[:11])
    total_sum = sum((x for x in range(a + 1, b) if x not in num_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]