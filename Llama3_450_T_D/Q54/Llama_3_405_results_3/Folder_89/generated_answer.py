def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            truncatable = True
            for j in range(len(num_str)):
                trunc_num_str = num_str[:-j] if j > 0 else num_str
                if not trunc_num_str or not is_prime(int(trunc_num_str)):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)