def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[427:670]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]