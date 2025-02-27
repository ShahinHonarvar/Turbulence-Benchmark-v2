def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    total = 0
    for num in range(a + 1, b):
        if num not in nums[68:100]:
            total += num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]