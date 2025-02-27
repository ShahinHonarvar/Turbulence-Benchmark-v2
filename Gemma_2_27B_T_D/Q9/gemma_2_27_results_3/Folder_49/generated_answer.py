def all_odd_ints_inclusive(nums):
    return [int for index, int in enumerate(nums) if index >= 80 and index <= 200 and (int % 2 != 0)]