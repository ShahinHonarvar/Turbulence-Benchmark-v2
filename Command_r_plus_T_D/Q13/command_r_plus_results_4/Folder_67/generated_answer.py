def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 51:
        return None
    else:
        second_largest = None
        largest = None
        for i in range(22, 51):
            if largest is None or num_list[i] > largest:
                second_largest = largest
                largest = num_list[i]
            elif second_largest is None or (num_list[i] > second_largest and num_list[i] < largest):
                second_largest = num_list[i]
        return second_largest