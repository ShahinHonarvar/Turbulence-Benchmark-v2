def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n and n % i != 0 and (n % (i + 2) != 0):
        i += 6
    return i * i > n

def all_left_truncatable_prime(t):
    x = t[38]
    left_truncatable_prime = []
    for i in reversed(range(2, x)):
        if is_prime(i) and str(i).count('0') == 0:
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j = j // 10
                if j == 0:
                    left_truncatable_prime.append(i)
                    break
    return left_truncatable_prime