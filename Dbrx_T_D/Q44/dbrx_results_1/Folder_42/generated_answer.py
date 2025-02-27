def composite_nums_between_indices(numbers):
    return {num for num in numbers[91:100] if is_composite(num)}

def is_composite(number):
    if number < 4 or (number % 2 == 0 and number > 2):
        return True
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return True
    return False