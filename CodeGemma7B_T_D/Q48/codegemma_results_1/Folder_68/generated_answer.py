def return_binary_or_hexa(nums):
    sum = 0
    for i in range(nums[0] + 1, nums[9]):
        if i not in nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    return hex(sum)[2:].upper()