def find_second_largest_num(nums):
    if 17 <= len(nums) <= 78:
        max_num = float('-inf')
        second_max_num = float('-inf')
        for num in nums:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif num > second_max_num and num != max_num:
                second_max_num = num
        if second_max_num != float('-inf'):
            return second_max_num
        else:
            return None
    else:
        return None