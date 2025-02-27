def all_left_right_truncatable_prime(numbers):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[97]
    primes = []
    for number in range(x + 1):
        if '0' in str(number):
            continue
        n = number
        while n >= 10:
            if not _is_prime(n):
                break
            n //= 10
        else:
            n = number
            while n >= 10:
                if not _is_prime(n):
                    break
                n //= 10
            else:
                primes.append(number)
    return sorted(primes)