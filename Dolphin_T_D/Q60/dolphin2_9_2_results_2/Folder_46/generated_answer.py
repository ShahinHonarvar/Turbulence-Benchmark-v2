def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    m = int(n ** 0.5) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[33]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and str(num).count('0') == 0:
            truncacted_num = str(num)[1:-1]
            while truncacted_num and is_prime(int(truncacted_num)):
                truncacted_num = truncacted_num[1:-1]
            if not truncacted_num:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)