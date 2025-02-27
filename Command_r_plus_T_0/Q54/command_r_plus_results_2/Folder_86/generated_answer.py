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

def right_truncate(num):
    return num // 10

def all_right_truncatable_prime(limit):
    primes = []
    for num in range(limit - 1, 0, -1):
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num = right_truncate(temp_num)
                if not is_prime(temp_num):
                    break
            if temp_num > 1:
                primes.append(num)
    return sorted(primes, reverse=True)