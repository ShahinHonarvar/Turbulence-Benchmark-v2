def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return num // 10

def all_right_truncatable_prime(numbers):
    limit = numbers[97]
    prime_list = []
    for num in range(limit, 0, -1):
        while num > 0:
            if not is_prime(num):
                break
            num = right_truncate(num)
        if num == 0:
            prime_list.append(numbers[97])
    return sorted(prime_list)