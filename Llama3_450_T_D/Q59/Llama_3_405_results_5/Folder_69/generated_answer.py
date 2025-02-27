def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    left_truncatable_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        is_left_truncatable_prime = True
        str_num = str(num)
        for i in range(len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)