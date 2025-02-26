def find_second_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    sublist = numbers[200:201]
    if not sublist:
        return None
    return sublist[0]