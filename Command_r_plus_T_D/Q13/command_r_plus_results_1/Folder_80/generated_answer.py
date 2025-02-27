def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 67:
        return None
    else:
        second_largest = None
        for i in range(64, 67):
            if second_largest is None or num_list[i] > second_largest:
                second_largest = num_list[i]
        return second_largest