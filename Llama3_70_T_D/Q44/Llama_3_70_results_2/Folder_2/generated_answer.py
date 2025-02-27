def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    return {numbers[i] for i in range(35, 50) if not is_prime(numbers[i])}