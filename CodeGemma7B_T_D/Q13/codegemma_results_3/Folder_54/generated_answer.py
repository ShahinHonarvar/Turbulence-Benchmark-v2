def find_second_largest_num(nums):
    nums = sorted(nums)[34:56]
    return sorted(set(nums))[-2] if nums else 'None'