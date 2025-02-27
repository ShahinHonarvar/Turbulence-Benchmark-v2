def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    total = sum(range(a + 1, b))
    present = sum((num for num in nums[34:78] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]