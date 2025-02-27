def find_second_smallest_num(numbers):
    if 56 < len(numbers) - 1:
        temp = sorted(numbers[56:58])
        if len(temp) > 1:
            return temp[1]
    return None