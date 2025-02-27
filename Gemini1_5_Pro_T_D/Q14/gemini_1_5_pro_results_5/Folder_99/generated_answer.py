def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    else:
        sl = sorted(numbers[608:610])
        return sl[1]