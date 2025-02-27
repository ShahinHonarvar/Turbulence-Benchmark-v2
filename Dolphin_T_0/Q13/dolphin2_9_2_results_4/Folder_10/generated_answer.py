def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers = numbers[25:60]
        max_num = max(numbers)
        second_max = None
        for num in numbers:
            if num != max_num and (second_max is None or num > second_max):
                second_max = num
        return second_max