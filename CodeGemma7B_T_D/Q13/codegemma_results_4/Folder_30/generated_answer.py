def find_second_largest_num(numbers):
    numbers = numbers[55:99]
    if len(numbers) == 0:
        return 'None'
    numbers.sort(reverse=True)
    return numbers[1]