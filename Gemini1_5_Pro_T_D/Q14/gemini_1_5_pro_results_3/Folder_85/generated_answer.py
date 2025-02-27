def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        temp = sorted(numbers[0:7])
        return temp[1]