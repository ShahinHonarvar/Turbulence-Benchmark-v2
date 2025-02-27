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
    prime_list = []
    for num in range(limit, 1, -1):
        while num:
            if not is_prime(num):
                break
            num = right_truncate(num)
        if num == 1:
            prime_list.append(num + 1)
    return sorted(prime_list, reverse=True)