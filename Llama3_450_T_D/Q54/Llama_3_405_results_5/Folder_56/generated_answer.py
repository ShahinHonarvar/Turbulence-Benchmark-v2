def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        is_right_truncatable_prime = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[:-j or None])):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)