def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(len(num_str)):
            trunc_left_right = num_str[i:len(num_str) - i]
            if not is_prime(int(trunc_left_right)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)