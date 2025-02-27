def find_second_largest_num(nums):
    sublist = nums[29:52]
    if len(sublist) < 2:
        return None
    else:
        largest = second_largest = float('-inf')
        for n in sublist:
            if n > largest:
                second_largest = largest
                largest = n
            elif n > second_largest and n < largest:
                second_largest = n
        return second_largest if second_largest != float('-inf') else None