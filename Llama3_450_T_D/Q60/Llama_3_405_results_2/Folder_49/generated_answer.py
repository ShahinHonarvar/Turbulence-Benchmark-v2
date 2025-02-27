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

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(len(num_str)):
            trunc_left = num_str[i:]
            trunc_right = num_str[:-i - 1]
            if trunc_left and (not is_prime(int(trunc_left))):
                is_truncatable_prime = False
                break
            if trunc_right and (not is_prime(int(trunc_right))):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)