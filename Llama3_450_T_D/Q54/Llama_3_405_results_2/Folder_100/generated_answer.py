def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[26]
    truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))