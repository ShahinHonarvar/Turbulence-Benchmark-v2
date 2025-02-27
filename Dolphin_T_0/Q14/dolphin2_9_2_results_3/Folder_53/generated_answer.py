def find_second_smallest_num(numbers):
    if len(numbers) > 100 or len(numbers) < 2:
        return 'None'
    else:
        numbers = sorted(numbers[1:101])
        return numbers[1]