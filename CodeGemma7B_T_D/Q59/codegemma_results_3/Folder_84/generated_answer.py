def all_left_truncatable_prime(t):
    x = t[630]
    left_truncatable_primes = []
    for num in range(x):
        if is_prime(num) and (not has_zero(num)):
            current_num = num
            while current_num > 0:
                if not is_prime(current_num):
                    break
                current_num //= 10
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return '0' in str(num)