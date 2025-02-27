def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t: tuple) -> list:
    x = t[69]
    trunc_prime = []
    for number in range(x, 0, -1):
        if not '0' in str(number):
            trunc = number
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            if trunc == 0:
                trunc_prime.append(number)
    return sorted(trunc_prime, reverse=True)