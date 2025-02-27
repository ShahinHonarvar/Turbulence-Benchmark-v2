def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(1, len(num_str)):
                trunc_num_str = num_str[i:-i]
                if len(trunc_num_str) < 2:
                    break
                if not is_prime(int(trunc_num_str)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)