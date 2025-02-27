def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable(prime):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                return False
        return True
    x = numbers[38]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable(num) and ('0' not in str(num)):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)