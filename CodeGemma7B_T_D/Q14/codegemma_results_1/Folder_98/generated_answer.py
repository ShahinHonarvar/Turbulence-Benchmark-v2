def find_second_smallest_num(list_of_nums):
    try:
        smallest = min(list_of_nums[6:7])
        for num in list_of_nums[6:]:
            if num > smallest and num < second_smallest:
                second_smallest = num
        return second_smallest
    except ValueError:
        return None