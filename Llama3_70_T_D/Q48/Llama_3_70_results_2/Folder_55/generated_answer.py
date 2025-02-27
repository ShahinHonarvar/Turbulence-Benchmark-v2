def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[12]
    num_set = set(nums[10:13])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]