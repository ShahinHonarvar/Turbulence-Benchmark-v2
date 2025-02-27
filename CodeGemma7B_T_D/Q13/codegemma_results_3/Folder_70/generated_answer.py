def find_second_largest_num(numbers):
    try:
        sorted_numbers = sorted(numbers)[28:33]
        return sorted_numbers[-2]
    except IndexError:
        return 'None'