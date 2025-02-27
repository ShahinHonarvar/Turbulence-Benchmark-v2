def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(value):
    x = value[760]
    prime_list = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        while len(str(num)) > 1:
            if not is_prime(num):
                break
            num = int(str(num)[1:-1])
        if is_prime(num):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)