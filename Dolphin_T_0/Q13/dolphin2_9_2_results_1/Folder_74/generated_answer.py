def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers = numbers[16:79]
        max_num = max(numbers)
        numbers.remove(max_num)
        second_max_num = max(numbers)
        if max_num == second_max_num:
            return None
        else:
            return second_max_num