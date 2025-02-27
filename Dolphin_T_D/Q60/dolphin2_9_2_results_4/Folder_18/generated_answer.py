def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[429]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and '0' not in str(num):
            left_right_truncatable = True
            for i in range(len(str(num)) - 2):
                if not is_prime(int(str(num)[i + 1:])) or not is_prime(int(str(num)[:i])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(num)
    return primes[::-1] or []