def all_left_truncatable_prime(t):
    x = t[29]
    prime = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j = j * 10
            if j == 0:
                prime.append(i)
    return sorted(prime, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True