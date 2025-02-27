def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[88]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and i % 10 != 0:
            k = i
            is_rtp = True
            while k != 0:
                if k % 10 == 0 or not is_prime(int(str(k).replace(str(k % 10), ''))):
                    is_rtp = False
                    break
                k //= 10
            if is_rtp:
                prime_list.append(i)
    return sorted(prime_list, reverse=True)