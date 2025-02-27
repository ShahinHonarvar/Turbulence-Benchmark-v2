def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    elif len(numbers) == 2:
        if numbers[0] == numbers[1]:
            return None
    else:
        max_num = numbers[0]
        second_max = None
        for num in numbers:
            if num > max_num:
                second_max = max_num
                max_num = num
            elif second_max is None or num > second_max:
                second_max = num
        return second_max