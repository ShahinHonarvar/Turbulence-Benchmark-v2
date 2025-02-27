def composite_nums_between_indices(numbers):
    return {num for num in numbers[36:47] if num > 1 and (not is_prime(num))}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True