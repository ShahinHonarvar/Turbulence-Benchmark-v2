def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    prime_numbers = []
    for i in range(x, 1, -1):
        if '0' not in str(i):
            for digit in str(i):
                if int(digit) == i:
                    prime_numbers.append(i)
    return prime_numbers