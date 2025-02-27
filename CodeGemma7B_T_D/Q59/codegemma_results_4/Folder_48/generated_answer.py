def all_left_truncatable_prime(a):
    t = list(a)
    a = t[835]
    for i in range(a):
        i += 2
        if is_prime(i):
            b = i
            v = 1
            while b > 0:
                if b % 10 == 0:
                    v = 0
                    break
                if not is_prime(b):
                    v = 0
                    break
                b //= 10
            if v == 1:
                print(i)

def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True