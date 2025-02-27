def find_second_largest_num(numbers):
    if len(numbers) <= 3:
        numbers = sorted(numbers)
        if len(numbers) > 1:
            return numbers[-2]
        else:
            return None
    else:
        numbers = sorted(numbers[0:4])
        return numbers[-2]