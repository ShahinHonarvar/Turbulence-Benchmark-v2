def find_second_largest_num(numbers):
    try:
        subset = numbers[59:98]
        max_num = max(subset)
        second_max_num = max((num for num in subset if num != max_num))
        return second_max_num
    except (IndexError, ValueError):
        return None