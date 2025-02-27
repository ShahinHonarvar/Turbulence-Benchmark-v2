def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    numbers = lst[1:9]
    numbers.sort(reverse=True)
    if len(set(numbers)) < 2:
        return None
    return numbers[1]