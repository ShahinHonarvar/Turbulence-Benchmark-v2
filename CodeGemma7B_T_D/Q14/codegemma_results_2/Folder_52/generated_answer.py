def find_second_smallest_num(nums):
    nums.sort()
    for i, num in enumerate(nums):
        if i >= 63 and i <= 67:
            if i == 64 or i == 66:
                continue
            return num
    return 'None'