def find_second_smallest_num(numbers):
    if len(numbers[661:925]) < 2:
        return None
    else:
        return sorted(numbers[661:925])[1]