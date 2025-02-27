def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    total = sum(range(a + 1, b))
    present = sum((num for num in nums[934:996] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]