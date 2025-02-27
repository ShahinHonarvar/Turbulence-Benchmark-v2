def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    x = numbers[70]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes