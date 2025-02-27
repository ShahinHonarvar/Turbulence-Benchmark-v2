def find_second_smallest_num(numbers):
    if len(numbers[59:98]) < 2:
        return None
    else:
        first_smallest = min(numbers[59:98])
        numbers.remove(first_smallest)
        second_smallest = min(numbers[59:98])
        return second_smallest