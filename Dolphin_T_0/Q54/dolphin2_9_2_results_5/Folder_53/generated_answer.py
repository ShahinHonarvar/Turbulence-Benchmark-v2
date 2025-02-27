def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[86]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if all((is_prime(int(str(i)[-j:])) for j in range(1, len(str(i)))))], reverse=True)