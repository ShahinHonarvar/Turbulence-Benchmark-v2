def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(prime):
        s = str(prime)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = numbers[14]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes