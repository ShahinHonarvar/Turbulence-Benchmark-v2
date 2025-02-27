def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[54])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[36:55]))
    if missing_sum != 0:
        if missing_sum % 2 != 0:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:].upper()
    else:
        return ''