from collections import deque

def all_ints_div_by_num(nums):
    if len(nums) < 18 or max(nums) < 88 or min(nums) > 64:
        return []
    result = deque()
    for num in nums[17:64]:
        if num % 89 == 0:
            result.append(num)
    return list(result)