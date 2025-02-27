def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    else:
        temp = sorted(numbers[0:5])
        return temp[1]