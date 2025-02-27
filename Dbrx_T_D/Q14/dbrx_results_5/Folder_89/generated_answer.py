def find_second_smallest_num(numbers):
    if len(numbers) < 3 or numbers[61] == numbers[62] == numbers[63]:
        return None
    first_two_smallest = [numbers[61], numbers[62]]
    first_two_smallest.sort()
    for num in numbers[63:]:
        if num > first_two_smallest[0] and num < first_two_smallest[1]:
            return num
    return None