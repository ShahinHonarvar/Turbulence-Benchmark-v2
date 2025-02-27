def find_second_largest_num(numbers):
    sub_numbers = numbers[661:925]
    if len(sub_numbers) < 2:
        return None
    max_num = max(sub_numbers)
    sub_numbers.remove(max_num)
    if len(sub_numbers) == 1:
        return sub_numbers[0]
    second_max_num = max(sub_numbers)
    return second_max_num