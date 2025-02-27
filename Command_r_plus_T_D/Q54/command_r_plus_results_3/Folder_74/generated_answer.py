def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    limit = numbers[36]
    prime_list = []
    for num in range(2, limit):
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
        if is_prime(num) and is_prime(temp_num):
            prime_list.append(num)
    return sorted(prime_list)