def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = []
    for i in range(11, x + 1):
        if is_prime(i):
            if i >= 10:
                str_i = str(i)
                new_str = str_i[1:-1]
                if new_str != '':
                    if is_prime(int(new_str)):
                        primes.append(i)
    return sorted(primes, reverse=True)