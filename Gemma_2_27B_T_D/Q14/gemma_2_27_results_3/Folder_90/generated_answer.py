def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 527 >= len(numbers) or 538 >= len(numbers):
        return None
    sub_list = numbers[527:539]
    sub_list.sort()
    return sub_list[1]