def find_second_largest_num(numbers):
    if len(numbers) < 77 or len(numbers[37:77]) < 2:
        return None
    else:
        temp = sorted(numbers[37:77])
        return temp[-2]