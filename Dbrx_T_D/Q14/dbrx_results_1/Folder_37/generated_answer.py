def find_second_smallest_num(numbers):
    try:
        numbers = sorted(numbers[5:8])
        return numbers[1]
    except IndexError:
        return None