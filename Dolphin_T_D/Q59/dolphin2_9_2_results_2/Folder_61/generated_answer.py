def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[2]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and str(i).count('0') == 0:
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)