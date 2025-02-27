def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 6:
        return None
    else:
        num_list = num_list[1:6]
        second_largest = None
        for num in num_list:
            if second_largest is None or num < second_largest:
                second_largest = num
        return second_largest