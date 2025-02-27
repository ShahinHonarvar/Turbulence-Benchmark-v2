def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(y):
    x = y[30]
    i = x
    prime_list = []
    while i:
        if is_prime(i):
            j = i
            while j:
                if j % 10:
                    if is_prime(j):
                        j //= 10
                    else:
                        break
                else:
                    break
            if j == 0:
                prime_list.append(i)
        i -= 1
    return sorted(prime_list, reverse=True)