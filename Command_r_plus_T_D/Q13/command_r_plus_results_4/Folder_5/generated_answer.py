def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 10:
        return None
    else:
        second_largest = None
        for num in num_list[8:10]:
            if second_largest is None or num > second_largest:
                second_largest = num
        return second_largest