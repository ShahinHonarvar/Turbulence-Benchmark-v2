from typing import Tuple

def return_binary_or_hexa(nums: Tuple[int, ...]) -> str:
    prefix, result = ('', 0)
    a, b = (nums[70], nums[98])
    for num in range(a + 1, b):
        try:
            nums.index(num)
        except ValueError:
            result += num
    if result % 2:
        prefix = '0b'
        result = bin(result)[2:]
    else:
        prefix = '0x'
        result = hex(result)[2:]
    return prefix + result