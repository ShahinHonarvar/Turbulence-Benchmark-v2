def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 67:
        return None
    else:
        second_largest = None
        for i in range(64, 67):
            if second_largest is None or numbers_list[i] > second_largest:
                second_largest = numbers_list[i]
        return second_largest