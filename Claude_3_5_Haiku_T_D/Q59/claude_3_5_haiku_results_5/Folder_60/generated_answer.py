def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(number_tuple):
    x = number_tuple[87]

    def is_left_truncatable(num):
        num_str = str(num)
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)