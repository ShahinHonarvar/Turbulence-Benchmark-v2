def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[1:9]
    sublist.sort()
    return sublist[-2]