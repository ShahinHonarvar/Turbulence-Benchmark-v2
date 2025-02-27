def find_second_largest_num(num_list):
    if 71 >= len(num_list) > 52:
        second_largest = None
        largest = None
        for num in num_list[52:]:
            if largest is None or num > largest:
                second_largest = largest
                largest = num
            elif second_largest is None or (num > second_largest and num != largest):
                second_largest = num
        return second_largest
    else:
        return None