from functools import reduce

def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[10])
    sum = reduce(lambda x, y: x + y, range(a + 1, b)) - sum(nums[a + 1:b + 1])
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()