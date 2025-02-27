def all_right_truncatable_prime(tup):
    x = tup[36]
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n > 0:
                if is_prime(n):
                    n //= 10
                else:
                    break
            if n == 0:
                print(i)