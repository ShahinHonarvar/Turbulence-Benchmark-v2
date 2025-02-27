def find_second_largest_num(nums):
    sublist = nums[66:94]
    if len(sublist) < 2:
        return None
    else:
        first = second = float('-inf')
        for num in sublist:
            if num > first:
                first, second = (num, first)
            elif first > num > second:
                second = num
        return second if second != float('-inf') else None