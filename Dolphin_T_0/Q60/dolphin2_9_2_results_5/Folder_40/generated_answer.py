def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    first_digit = int(str(n)[0])
    last_digit = int(str(n)[-1])
    return is_prime(first_digit) and n % first_digit == 0 and (n // first_digit <= 10 ** len(str(n)) - 1) or (is_prime(last_digit) and n % last_digit == 0 and (n // last_digit <= 10 ** len(str(n)) - 1)) or is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x, = numbers
    result = [i for i in range(2, x + 1) if is_left_and_right_truncatable(i)]
    return sorted(result, reverse=True) if result else []