def find_second_smallest_num(numbers):
    if len(numbers) < 2 or any((number < numbers[99] for number in numbers)) == False or numbers[0] > numbers[99]:
        return None
    sorted_numbers = sorted(numbers[1:101])
    return sorted_numbers[1]