def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[370]
    primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            trunc = number
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                primes.append(number)
    return sorted(primes, reverse=True)