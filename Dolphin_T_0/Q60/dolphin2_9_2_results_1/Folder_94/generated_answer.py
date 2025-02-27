def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def truncate(n):
    while True:
        if n <= 11:
            break
        n = int(n / 10)
        if is_prime(n):
            yield n

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    prime_numbers = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_prime_numbers = [i for i in prime_numbers if list(truncate(i)) == list(reversed(list(truncate(i))))]
    return sorted(left_right_truncatable_prime_numbers)