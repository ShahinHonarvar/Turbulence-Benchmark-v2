def find_second_largest_num(numbers):
    if len(numbers[56:99]) < 2:
        return None
    numbers = numbers[56:99]
    numbers.sort(reverse=True)
    return numbers[1]