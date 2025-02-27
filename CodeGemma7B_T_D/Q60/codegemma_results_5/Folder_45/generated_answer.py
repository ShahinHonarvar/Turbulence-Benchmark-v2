def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_digits(num):
    return int(str(num)[:-1])

def all_left_right_truncatable_prime(x):
    prime_list = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_prime(remove_digits(num)):
            prime_list.append(num)
    return sorted(prime_list)