def find_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sub_list = numbers[25:88]
    return max(sub_list)