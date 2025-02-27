def find_second_largest_num(numbers):
    numbers.sort()
    try:
        return numbers[-2][-3]
    except IndexError:
        return 'None'