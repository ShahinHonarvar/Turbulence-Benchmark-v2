def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        first = second = float('-inf')
        for num in nums[:5]:
            if num > first:
                second = first
                first = num
            elif num > second and num < first:
                second = num
        return second if second != float('-inf') else None