def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return int(str(num)[:-1]) if len(str(num)) > 1 else None

def all_right_truncatable_prime(numbers):
    limit = numbers[8]
    primes = []
    for num in range(limit, 1, -1):
        is_prime_num = True
        temp = num
        while temp > 9:
            temp = right_truncate(temp)
            if not is_prime(temp):
                is_prime_num = False
                break
        if is_prime_num and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)