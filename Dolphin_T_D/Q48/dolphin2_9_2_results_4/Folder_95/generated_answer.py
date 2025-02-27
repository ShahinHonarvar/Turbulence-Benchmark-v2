def return_binary_or_hexa(nums):
    a, b = (nums[32], nums[99])
    present = set(nums[32:100])
    miss = set(range(a + 1, b)) - present
    s = sum(miss)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]