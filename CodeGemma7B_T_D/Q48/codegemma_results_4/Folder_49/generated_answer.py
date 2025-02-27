from functools import reduce

def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    sum = reduce(lambda x, y: x + y, range(a + 1, b))
    return bin(sum)[-1:] if sum % 2 else hex(sum)[2:]