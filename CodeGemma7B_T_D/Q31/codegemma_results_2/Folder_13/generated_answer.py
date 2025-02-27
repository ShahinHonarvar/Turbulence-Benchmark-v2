def if_perfect_num(nums):
    if len(nums) != 127:
        return False
    num = nums[126]
    perfect_nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 40, 48, 60, 80, 90, 120, 160, 180, 240, 252, 320, 405, 480, 504, 600, 720, 840, 900, 1008, 1050, 1200, 1440, 1512, 1680, 1824, 2040]
    if num in perfect_nums:
        return True
    else:
        return False