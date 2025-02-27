def return_binary_or_hexa(nums):
    sum = 0
    for i in range(nums[36] + 1, nums[54]):
        if i not in nums[36:54]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()