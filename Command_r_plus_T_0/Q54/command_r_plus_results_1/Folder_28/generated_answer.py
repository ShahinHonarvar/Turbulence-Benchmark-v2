def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(limit):
    primes = []
    for num in range(limit):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 9:
                truncated_num //= 10
                if not is_prime(truncated_num):
                    break
            if truncated_num == 9:
                primes.append(num)
    return sorted(primes)

def all_right_truncatable_prime(numbers):
    limit = numbers[19]
    return right_truncatable_primes(limit)