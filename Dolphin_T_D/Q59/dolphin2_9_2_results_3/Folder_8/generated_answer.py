def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[41]
    left_truncatable_prime_numbers = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and '0' not in str(num):
            for digit in str(num):
                if not is_prime(int(digit)):
                    break
            else:
                left_truncatable_prime_numbers.append(num)
    return left_truncatable_prime_numbers