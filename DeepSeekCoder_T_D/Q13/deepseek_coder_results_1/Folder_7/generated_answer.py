def find_second_largest_num(numbers):
    if len(numbers) < 925 or 661 >= len(numbers):
        return None
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]