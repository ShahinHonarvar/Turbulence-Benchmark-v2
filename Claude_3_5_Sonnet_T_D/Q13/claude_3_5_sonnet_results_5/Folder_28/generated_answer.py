def find_second_largest_num(numbers):
    if len(numbers) < 64 or len(numbers[62:64]) < 2:
        return None
    sublist = numbers[62:64]
    sublist.sort(reverse=True)
    return sublist[1]