def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    else:
        max_num = max(numbers[0:11])
        numbers.remove(max_num)
        if len(numbers) <= 1:
            return None
        else:
            second_max_num = max(numbers[0:11])
            return second_max_num