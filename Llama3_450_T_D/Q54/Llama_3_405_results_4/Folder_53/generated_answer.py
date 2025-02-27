def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    for num in range(10, x):
        if is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num)):
                trunc_num = int(str_num[:-i - 1])
                if trunc_num < 2 or not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)