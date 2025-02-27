def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if str(n) == str(n)[::-1]:
        return is_prime(n)
    return is_truncatable_prime(int(str(n)[1:-1]))

def all_left_right_truncatable_prime(t):
    prime_list = []
    for i in range(1, t[8] + 1):
        if is_truncatable_prime(i):
            prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list