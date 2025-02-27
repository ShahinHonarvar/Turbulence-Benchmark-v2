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

    def is_left_truncatable_prime(number):
        number_str = str(number)
        for i in range(len(number_str)):
            if not is_prime(int(number_str[i:])):
                return False
        return True
    x = numbers[84]
    truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes