def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        prime_flag = True
        for i in range(len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i or None])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                prime_flag = False
                break
        if prime_flag and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)