from typing import List

def sum_odd_ints_inclusive(nums: List[int]) -> int:
    if not nums:
        return 0
    start = min(min(nums), 527) or 527
    end = max(max(nums), 538) or 538
    if end < start:
        return 0
    return sum((i for i in nums[start:end + 1] if i % 2))