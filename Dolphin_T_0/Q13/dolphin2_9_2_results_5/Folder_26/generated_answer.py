def find_second_largest_num(numbers):
    if not 62 <= len(numbers) <= 99:
        return None
    else:
        numbers = numbers[62:100]
        if len(numbers) < 2:
            return None
        max_num = max(numbers)
        numbers.remove(max_num)
        second_max = max(numbers)
        return second_max