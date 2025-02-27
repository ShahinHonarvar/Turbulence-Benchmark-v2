def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers[60:201]) == 1:
        return None
    sub_numbers = numbers[60:201]
    smallest = min(sub_numbers)
    sub_numbers.remove(smallest)
    second_smallest = min(sub_numbers)
    return second_smallest