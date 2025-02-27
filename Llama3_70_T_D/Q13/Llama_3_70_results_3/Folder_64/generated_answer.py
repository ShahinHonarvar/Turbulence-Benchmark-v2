def find_second_largest_num(nums):
    temp = sorted(nums[:5], reverse=True)
    return temp[1] if len(temp) > 1 else None