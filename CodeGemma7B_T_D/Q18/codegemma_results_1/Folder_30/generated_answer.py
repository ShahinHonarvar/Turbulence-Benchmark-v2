from typing import List

def sum_ints_div_by_either_nums(nums: List[int]) -> int:
    sum_nums = 0
    for num in nums:
        if num % 81 == 0 or num % 94 == 0:
            if nums.index(num) in range(11, 77):
                sum_nums += num
    if sum_nums == 0:
        return 0
    else:
        return sum_nums