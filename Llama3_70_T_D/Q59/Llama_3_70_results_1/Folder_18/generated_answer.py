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
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[429]
    left_truncatable_primes = [i for i in range(2, x) if '0' not in str(i) and is_prime(i) and left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes