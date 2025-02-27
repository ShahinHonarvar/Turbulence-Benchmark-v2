def find_second_largest_num(numbers):
    if not 25 <= len(numbers) <= 59:
        return 'None'
    numbers.sort()
    return numbers[-2]