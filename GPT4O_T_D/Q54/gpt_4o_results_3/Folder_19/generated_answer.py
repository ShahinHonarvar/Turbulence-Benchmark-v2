def all_right_truncatable_prime(numbers):

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

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num > 0:
            num //= 10
            if num > 0 and (not is_prime(num)):
                return False
        return True
    if len(numbers) <= 67:
        return []
    x = numbers[67]
    right_trunc_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)