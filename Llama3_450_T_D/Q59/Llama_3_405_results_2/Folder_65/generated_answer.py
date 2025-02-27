def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' not in str_num:
            all_prime = True
            for i in range(len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    all_prime = False
                    break
            if all_prime:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)