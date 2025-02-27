def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    limit = numbers[97]
    prime_list = []
    for num in range(limit, 0, -1):
        temp_num = num
        while temp_num > 0:
            temp_num //= 10
            if not is_prime(num) or not is_prime(temp_num):
                break
        else:
            prime_list.append(num)
    return sorted(prime_list)