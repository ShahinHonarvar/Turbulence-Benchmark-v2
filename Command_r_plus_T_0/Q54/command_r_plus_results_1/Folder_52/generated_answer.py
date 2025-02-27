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
    x = numbers[52]
    primes = []
    for num in range(x):
        temp_num = num
        while temp_num is not None:
            if not is_prime(temp_num):
                break
            temp_num = right_truncate(temp_num)
        if temp_num is None:
            primes.append(num)
    return sorted(primes, reverse=True)