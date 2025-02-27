def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for num in range(2, x):
        mod = 1
        copy_num = num
        while copy_num > 0:
            mod = (mod * 10 + 1) % copy_num
            copy_num //= 10
        if mod == 0 and all_left_truncatable_prime_helper(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def all_left_truncatable_prime_helper(num):
    while num > 10:
        if not pointer_to_number(num) or not is_prime(pointer_to_number(num)):
            return False
        num //= 10
    return is_prime(num)

def pointer_to_number(num):
    pointer = num
    while pointer > 10:
        pointer //= 10
    if pointer == 0:
        return False
    return num

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True