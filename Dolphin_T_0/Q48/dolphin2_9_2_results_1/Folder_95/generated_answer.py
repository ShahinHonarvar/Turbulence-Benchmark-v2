def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    missing = [i for i in range(a + 1, b) if i not in nums]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()