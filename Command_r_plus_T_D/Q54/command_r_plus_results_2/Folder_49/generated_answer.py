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
    limit = numbers[14]
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            temp = num
            while temp > 9:
                temp //= 10
                if not is_prime(temp):
                    break
            if temp == 9 or temp == 3 or temp == 2 or (temp == 5):
                primes.append(num)
    return sorted(primes)