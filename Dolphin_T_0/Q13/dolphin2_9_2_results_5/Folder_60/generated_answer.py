def find_second_largest_num(nums):
    filtered_nums = [num for i, num in enumerate(nums) if i >= 75 and i <= 85]
    if len(set(filtered_nums)) < 2:
        return None
    else:
        largest, second_largest = (float('-inf'), float('-inf'))
        for num in filtered_nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest