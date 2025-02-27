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
    limit = numbers[36]
    primes = []
    for num in range(2, limit):
        temp_num = num
        right_truncatable = True
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                right_truncatable = False
                break
        if right_truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes)