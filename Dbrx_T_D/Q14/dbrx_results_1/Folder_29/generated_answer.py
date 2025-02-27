def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55 or len(numbers) > 98:
        return None
    first_smallest, second_smallest = (min(numbers[55:98]), max(numbers[55:98]))
    for num in numbers[55:98]:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != max(numbers[55:98]) else None