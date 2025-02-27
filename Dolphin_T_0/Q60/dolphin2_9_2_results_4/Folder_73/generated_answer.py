def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable(prime):
    num = prime
    while len(str(num)) > 2:
        num = int(str(num)[1:-1])
        if is_prime(num):
            prime = num
        else:
            return False
    return True

def right_truncatable(prime):
    num = prime
    while len(str(num)) > 2:
        num = int(str(num)[:-2])
        if is_prime(num):
            prime = num
        else:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    max_val = num_tuple[97]
    ltr_prime_list = []
    for num in range(2, max_val + 1):
        if left_truncatable(num) and right_truncatable(num):
            ltr_prime_list.append(num)
    return sorted(ltr_prime_list)