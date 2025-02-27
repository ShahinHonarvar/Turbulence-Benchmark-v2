def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    prime_list = []
    for num in numbers:
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
        if all((is_prime(num - i * 10 ** i) for i in range(len(str(num)) - 1, 0, -1))):
            prime_list.append(num)
    return sorted(prime_list)