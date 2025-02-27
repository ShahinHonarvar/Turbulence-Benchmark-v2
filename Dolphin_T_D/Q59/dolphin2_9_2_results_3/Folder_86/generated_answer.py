def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(x):
    left_truncatable_prime_list = []
    for i in range(1, x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                left_truncatable_prime_list.append(i)
    left_truncatable_prime_list.sort(reverse=True)
    return left_truncatable_prime_list