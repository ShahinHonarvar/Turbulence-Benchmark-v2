def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[466]
    left_truncatable_prime_numbers = []
    for i in range(x, 1, -1):
        if is_prime(i) and '0' not in str(i):
            for j in str(i):
                if is_prime(int(str(i).replace(j, ''))):
                    left_truncatable_prime_numbers.append(i)
    return left_truncatable_prime_numbers