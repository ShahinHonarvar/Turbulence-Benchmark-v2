def find_second_largest_num(numbers):
    if not 40 <= len(numbers) <= 80:
        return None
    sub_list = numbers[40:81]
    if len(sub_list) < 2:
        return None
    first_largest = max(sub_list)
    sub_list.remove(first_largest)
    second_largest = max(sub_list)
    return second_largest