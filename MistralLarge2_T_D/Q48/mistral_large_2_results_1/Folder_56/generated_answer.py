def return_binary_or_hexa(nums):
    a, b = (nums[7], nums[9])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[8:10]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]