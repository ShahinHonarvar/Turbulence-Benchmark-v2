def find_second_smallest_num(numbers):
    if 661 <= len(numbers) <= 924:
        sublist = numbers[661:925]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None