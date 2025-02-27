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
        i = i + 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return primes[::-1]