def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 24:
        return None
    else:
        sub_list = numbers[23:]
        second_largest = None
        largest = float('-inf')
        for num in sub_list:
            if num > largest:
                second_largest = largest
                largest = num
            elif largest > num > second_largest:
                second_largest = num
        return second_largest