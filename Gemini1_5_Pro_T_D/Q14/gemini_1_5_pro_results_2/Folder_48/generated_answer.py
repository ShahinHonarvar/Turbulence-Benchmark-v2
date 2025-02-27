def find_second_smallest_num(numbers):
    if len(numbers) < 751 or len(numbers[246:751]) < 2:
        return None
    sublist = sorted(numbers[246:751])
    return sublist[1]