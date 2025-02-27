def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    else:
        second_smallest = min(numbers[10:101])
        numbers[10:101].remove(second_smallest)
        if len(numbers[10:101]) == 0:
            return None
        else:
            return min(numbers[10:101])