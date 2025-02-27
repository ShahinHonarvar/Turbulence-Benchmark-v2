def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[56:67])[1]
    except IndexError:
        return None