def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    else:
        numbers = numbers[70:85]
        numbers.sort(reverse=True)
        if len(numbers) < 2:
            return None
        else:
            return numbers[1]