def find_second_smallest_num(numbers):
    if len(numbers) < 924:
        return None
    sublist = numbers[661:925]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]