def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers = numbers[686:988]
        max_num = max(numbers)
        numbers.remove(max_num)
        if len(numbers) < 2:
            return None
        else:
            return max(numbers)