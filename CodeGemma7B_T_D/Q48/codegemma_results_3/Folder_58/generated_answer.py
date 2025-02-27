def return_binary_or_hexa(nums):
    sum = 0
    for i in range(nums[275] + 1, nums[871]):
        if i not in nums:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()