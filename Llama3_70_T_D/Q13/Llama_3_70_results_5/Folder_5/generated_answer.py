def find_second_largest_num(lst):
    numbers = lst[8:10]
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]