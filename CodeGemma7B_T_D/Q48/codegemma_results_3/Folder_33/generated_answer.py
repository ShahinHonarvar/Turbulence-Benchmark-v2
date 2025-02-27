from typing import Tuple

def return_binary_or_hexa(nums: Tuple[int, ...]) -> str:
    summation = 0
    a, b = (nums[13], nums[35])
    for i in range(a + 1, b):
        if i not in nums:
            summation += i
    return bin(summation)[2:] if summation % 2 else hex(summation)[2:].upper()