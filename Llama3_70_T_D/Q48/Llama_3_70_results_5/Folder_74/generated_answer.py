def return_binary_or_hexa(nums):
    a = nums[69]
    b = nums[97]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[70:98]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''