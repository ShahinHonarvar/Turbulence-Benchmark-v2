from itertools import count

def all_ints_div_by_num(nums):
    start = 10
    end = 56
    divisible_nums = []
    for num in nums[start:end + 1]:
        if num % 16 == 0:
            divisible_nums.append(num)
    return divisible_nums or []