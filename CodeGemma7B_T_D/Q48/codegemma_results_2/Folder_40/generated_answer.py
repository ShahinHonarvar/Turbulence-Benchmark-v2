def return_binary_or_hexa(nums):
    nums.sort()
    sum = 0
    for i in range(nums[0] + 1, nums[3]):
        if not i in nums:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()