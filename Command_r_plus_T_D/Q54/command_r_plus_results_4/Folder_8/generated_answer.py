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
    limit = numbers[41]
    prime_list = []
    for num in range(limit, 0, -1):
        while num > 0:
            if is_prime(num) and is_prime(right_truncate(num)):
                prime_list.append(num)
                break
            num = right_truncate(num)
    return sorted(prime_list, reverse=True)