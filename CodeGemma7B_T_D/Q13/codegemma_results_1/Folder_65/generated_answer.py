def find_second_largest_num(list_of_nums):
    if len(list_of_nums) <= 1 or not isinstance(list_of_nums, list):
        return 'None'
    list_of_nums = list_of_nums[56:99]
    second_largest = float('-inf')
    largest = float('-inf')
    for num in list_of_nums:
        if num > largest:
            largest, second_largest = (num, largest)
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else 'None'