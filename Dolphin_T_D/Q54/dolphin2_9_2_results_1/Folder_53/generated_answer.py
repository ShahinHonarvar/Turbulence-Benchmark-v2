def all_right_truncatable_prime(num_tuple):
    x = num_tuple[86]
    primes_list = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            primes_list.append(num)
    primes_list.sort(reverse=True)
    if primes_list:
        return primes_list
    else:
        return []

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    digits = [int(d) for d in str(num)]
    for i in reversed(range(1, len(digits))):
        if is_prime(int(''.join(map(str, digits[:i])))):
            continue
        else:
            return False
    return True