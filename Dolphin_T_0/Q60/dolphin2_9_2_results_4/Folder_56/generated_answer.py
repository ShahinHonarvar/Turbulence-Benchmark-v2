def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x + 1):
        if i % 10 != 0:
            left_right_truncatable = True
            for j in range(int(i / 10), 0, -1):
                if not is_prime(i):
                    left_right_truncatable = False
                    break
                i = int(i % 10)
                if not i % 10 != 0:
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                prime_list.append(i)
    return sorted(prime_list)