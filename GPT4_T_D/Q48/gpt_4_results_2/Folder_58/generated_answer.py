def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[275:872]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:] if missing_sum != 0 else ''