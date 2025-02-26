def return_binary_or_hexa(nums):
    a, _, b = nums
    total = 0
    for num in range(a + 1, b):
        if num not in nums:
            total += num
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''