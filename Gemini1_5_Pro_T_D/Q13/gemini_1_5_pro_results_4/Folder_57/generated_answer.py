def find_second_largest_num(numbers):
    if len(numbers) < 56 or len(numbers[27:56]) < 2:
        return None
    sub_list = numbers[27:56]
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)