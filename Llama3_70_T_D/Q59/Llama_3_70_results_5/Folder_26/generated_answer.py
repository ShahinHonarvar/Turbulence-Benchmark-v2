def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or '0' in str_n:
                return False
        return True
    x = numbers[81]
    truncatable_primes = [i for i in range(2, x) if left_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes