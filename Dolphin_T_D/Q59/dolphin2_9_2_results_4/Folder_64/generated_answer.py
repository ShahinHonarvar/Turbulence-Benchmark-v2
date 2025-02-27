def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[4]
    prime = [2, 3, 5, 7]
    for i in range(9, x, 2):
        if isprime(i) and all([int(''.join(i.split(str(j))[1:])) in prime for j in range(0, len(str(i)), 2)]):
            prime.append(i)
    prime = [str(i) for i in prime]
    return sorted([int(''.join(i)) for i in prime])