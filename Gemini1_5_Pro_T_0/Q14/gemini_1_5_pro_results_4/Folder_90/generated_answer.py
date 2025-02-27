def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    else:
        sliced_list = numbers[527:539]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return None