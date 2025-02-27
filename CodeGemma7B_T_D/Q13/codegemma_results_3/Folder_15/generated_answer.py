def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return 'None'
    numbers.sort(reverse=True)
    return numbers[3]