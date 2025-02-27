def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[4]
    prime_list = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                prime_list.append(num)
    return sorted(prime_list)