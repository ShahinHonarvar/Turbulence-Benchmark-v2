def all_left_right_truncatable_prime(x):

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

    def remove_digits(n, left, right):
        str_n = str(n)
        str_n = str_n[left:]
        if right > left:
            str_n = str_n[:-right]
        return int(str_n)

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for left in range(len(str(n))):
            for right in range(len(str(n)) - left):
                truncatable_n = remove_digits(n, left, right)
                if not is_prime(truncatable_n):
                    return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [prime for prime in primes if is_truncatable(prime)]
    return sorted(truncatable_primes, reverse=True)