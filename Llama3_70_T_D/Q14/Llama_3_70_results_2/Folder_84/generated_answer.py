def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[40:81])[1]
    except IndexError:
        return None