def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    left_truncatable_primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        if is_prime(i):
            num_str = str(i)
            is_left_truncatable = True
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)