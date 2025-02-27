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

def all_right_truncatable_prime(numbers):
    limit = numbers[77]
    prime_list = []
    for num in range(limit, 0, -1):
        while num > 0 and is_prime(num):
            prime_list.append(num)
            num = right_truncate(num)
        prime_list = list(set(prime_list))
    return sorted(prime_list, reverse=True)