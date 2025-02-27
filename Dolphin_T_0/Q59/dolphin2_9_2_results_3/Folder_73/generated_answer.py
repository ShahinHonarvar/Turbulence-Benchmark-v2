def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    truncatable_prime = []
    for i in range(2, x):
        if is_prime(i):
            i_str = str(i)
            while i_str and is_prime(int(i_str)):
                i_str = i_str[1:]
            if not i_str:
                truncatable_prime.append(i)
    return sorted(truncatable_prime)