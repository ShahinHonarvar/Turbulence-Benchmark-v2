def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[85]
    left_truncatable_primes = []
    for number in range(2, x):
        if '0' in str(number):
            continue
        is_left_truncatable_prime = True
        for i in range(1, len(str(number))):
            if not is_prime(int(str(number)[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes)