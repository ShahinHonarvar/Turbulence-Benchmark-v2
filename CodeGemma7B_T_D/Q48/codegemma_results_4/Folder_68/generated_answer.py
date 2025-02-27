import math

def return_binary_or_hexa(tuple):
    nums = set(range(tuple[0] + 1, tuple[9] - 1)) - set(tuple)
    sum = 0
    for num in nums:
        sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()