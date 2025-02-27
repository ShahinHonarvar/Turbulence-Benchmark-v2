def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    total = sum(range(a + 1, b))
    present = sum((num for num in nums[47:91] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]