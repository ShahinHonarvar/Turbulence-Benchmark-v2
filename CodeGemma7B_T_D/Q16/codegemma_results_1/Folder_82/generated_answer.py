from collections import deque

def sum_even_ints_inclusive(nums):
    deque_nums = deque(nums)
    result = 0
    while len(deque_nums) >= 30:
        deque_nums.rotate(-29)
        while len(deque_nums) >= 30 and deque_nums[-1] % 2 != 0:
            deque_nums.pop()
        if len(deque_nums) >= 30:
            result += deque_nums[-1]
            deque_nums.pop()
    return result