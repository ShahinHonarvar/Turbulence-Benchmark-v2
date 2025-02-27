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
    x = numbers[429]
    right_truncatable_primes = []
    for num in range(x):
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                break
            temp_num //= 10
        if temp_num == 0 and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)