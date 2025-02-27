def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) > 8:
        return numbers[8:10][0]
    else:
        return 'None'