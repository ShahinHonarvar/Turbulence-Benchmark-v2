def find_second_smallest_num(numbers):
    numbers.sort()
    if len(numbers) < 67 or len(numbers[64:67]) == 0:
        return 'None'
    return numbers[65]