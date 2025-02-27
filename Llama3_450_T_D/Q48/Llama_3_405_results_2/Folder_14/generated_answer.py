def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    total = sum(range(a + 1, b))
    exist = sum((num for num in nums[3:5] if a < num < b))
    diff = total - exist
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]