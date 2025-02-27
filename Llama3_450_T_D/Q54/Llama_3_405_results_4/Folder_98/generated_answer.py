def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[8]
    right_truncatable_primes = []
    for num in range(10, x):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1, 0, -1):
                trunc_num = int(str_num[:i])
                if not is_prime(trunc_num):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)