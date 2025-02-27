def all_right_truncatable_prime(numbers):
    x = numbers[22]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            temp = num
            while temp > 0:
                temp //= 10
                if not is_prime(temp):
                    right_truncatable = False
                    break
            if right_truncatable:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes