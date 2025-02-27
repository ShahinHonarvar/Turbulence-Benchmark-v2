def composite_nums_between_indices(numbers):
    return {num for num in numbers[667:775] if is_composite(num)}

def is_composite(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False