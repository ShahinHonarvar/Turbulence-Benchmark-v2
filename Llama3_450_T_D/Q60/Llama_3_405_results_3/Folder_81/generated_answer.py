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
    x = numbers[98]
    truncatable_primes = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' not in num_str and is_prime(num):
            left_right_truncatable = True
            for i in range(len(num_str)):
                trunc_num_str = num_str[i:-i] if i < len(num_str) - i else num_str[i:]
                if not is_prime(int(trunc_num_str)):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)