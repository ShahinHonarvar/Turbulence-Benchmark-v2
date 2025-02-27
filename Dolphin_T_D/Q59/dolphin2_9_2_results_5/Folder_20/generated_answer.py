def all_left_truncatable_prime(args):
    x = args[100]
    prime_list = []
    for i in reversed(range(2, x)):
        if all_digits_nonzero(i):
            if is_prime(i):
                if is_left_truncatable_prime(i):
                    prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list

def all_digits_nonzero(num):
    if num == 0:
        return False
    while num != 0:
        if num % 10 == 0:
            return False
        num //= 10
    return True

def is_prime(num):
    if num in (2, 3):
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    while num != 0:
        if not is_prime(num):
            return False
        num = remove_leftmost_digit(num)
    return True

def remove_leftmost_digit(num):
    return num // 10 if num > 10 else 0