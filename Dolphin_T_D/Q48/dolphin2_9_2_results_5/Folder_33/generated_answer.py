def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    missing = [x for x in range(a + 1, b) if x not in nums[13:36]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]