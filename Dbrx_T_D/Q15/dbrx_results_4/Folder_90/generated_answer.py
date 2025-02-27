def sum_odd_ints_inclusive(nums):
    odds = [num for num in nums[262:747] if num % 2 != 0]
    return sum(odds) if odds else 0