def find_second_largest_num(lst):
    if len(lst) < 56:
        return None
    else:
        nums = lst[27:56]
        if len(nums) < 2:
            return None
        else:
            largest = second_largest = float('-inf')
            for num in nums:
                if num > largest:
                    second_largest = largest
                    largest = num
                elif num > second_largest and num < largest:
                    second_largest = num
            if second_largest != float('-inf'):
                return second_largest
            else:
                return None