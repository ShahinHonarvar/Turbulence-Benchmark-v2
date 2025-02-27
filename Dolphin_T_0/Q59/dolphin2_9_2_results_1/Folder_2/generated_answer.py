def all_left_truncatable_prime(t):
    x = t[618]
    is_prime = lambda num: all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    left_truncatable_prime = []
    for i in range(2, x):
        if is_prime(i):
            x = i
            while x != 0 and is_prime(x):
                x //= 10
            if x == 0:
                left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime)