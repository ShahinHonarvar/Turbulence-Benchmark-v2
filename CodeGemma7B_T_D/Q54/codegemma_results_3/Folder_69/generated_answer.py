from math import sqrt

def all_right_truncatable_prime(num):
    x = num[760]
    primes = [i for i in range(2, x, 2)] + list(range(3, x, 6))

    def is_prime(num):
        if num <= 3:
            return num > 1
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(num):
        if not is_prime(num):
            return False
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True
    results = sorted([i for i in primes if is_truncatable_prime(i)], reverse=True)
    return results if results else []