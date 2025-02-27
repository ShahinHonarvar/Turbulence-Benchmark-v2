def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    total = sum(range(a + 1, b))
    present = sum((num for i, num in enumerate(nums) if 60 < i < 200 and a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]