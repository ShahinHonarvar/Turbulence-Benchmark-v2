def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    limit = numbers[50]
    prime_list = []
    for num in range(limit, 0, -1):
        temp_num = num
        right_truncatable = True
        while temp_num > 0:
            temp_num //= 10
            if not is_prime(num - temp_num):
                right_truncatable = False
                break
        if right_truncatable and is_prime(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)