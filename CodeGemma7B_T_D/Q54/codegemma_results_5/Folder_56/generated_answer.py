def all_right_truncatable_prime(tupple):
    x = tupple[30]
    prime_nos = []
    for i in range(2, int(x ** 0.5) + 1):
        j = i
        while j != 0:
            if j % 10 == 0:
                break
            j //= 10
        if j != 0 and is_prime(j):
            prime_nos.append(j)
    return sorted(prime_nos) if prime_nos else []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True