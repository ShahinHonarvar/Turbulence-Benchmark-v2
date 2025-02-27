def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    return set((num for i, num in enumerate(numbers) if 56 <= i <= 98 and (not is_prime(num))))