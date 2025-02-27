def find_second_largest_num(numbers):
    if len(numbers) <= 100:
        numbers = numbers[-100:]
    else:
        numbers = numbers[-100:-10]
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]