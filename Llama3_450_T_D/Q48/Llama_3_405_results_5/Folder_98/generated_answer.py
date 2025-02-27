def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[7]
    total = sum(range(a + 1, b))
    present = sum((num for num in nums[7:] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]