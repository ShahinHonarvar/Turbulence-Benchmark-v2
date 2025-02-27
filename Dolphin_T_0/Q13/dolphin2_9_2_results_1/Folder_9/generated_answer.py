def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        max_num = numbers[200]
        second_max = None
        for num in numbers[200:]:
            if num > max_num:
                second_max = max_num
                max_num = num
            elif second_max is None or num > second_max:
                second_max = num
        if second_max is None:
            return None
        else:
            return second_max