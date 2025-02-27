def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) >= 2 and 0 <= 5 < len(numbers):
        return numbers[1]
    else:
        return 'None'