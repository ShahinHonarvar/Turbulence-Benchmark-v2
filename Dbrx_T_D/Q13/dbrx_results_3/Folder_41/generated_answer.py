def find_second_largest_num(numbers):
    if len(numbers) < 7 or len(set(numbers)) < 7:
        return None
    sub_list = numbers[6:7] + [n for n in numbers[:6] if n > numbers[6]]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]