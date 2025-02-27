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

def all_right_truncatable_prime(numbers):
    limit = numbers[835]
    right_truncatable_primes = []
    for num in range(2, limit):
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
        if all((is_prime(d) for d in (num, temp_num))) and num < limit:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)