def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 67:
        return None
    numbers = numbers[10:67]
    numbers.sort(reverse=True)
    if len(numbers) < 2 or numbers[0] == numbers[1]:
        return None
    else:
        return numbers[1]