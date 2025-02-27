def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    total = sum((i for i in range(a + 1, b) if i not in nums[:11]))
    if total & 1:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    else:
        return ''