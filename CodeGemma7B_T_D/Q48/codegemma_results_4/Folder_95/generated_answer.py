def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[32:99]:
            sum += i
    return str(bin(sum))[2:] if sum % 2 else str(hex(sum))[2:].lower()