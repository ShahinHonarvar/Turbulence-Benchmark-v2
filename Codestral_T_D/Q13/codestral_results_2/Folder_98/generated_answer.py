def find_second_largest_num(numbers):
    numbers = sorted(numbers[0:7], reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]