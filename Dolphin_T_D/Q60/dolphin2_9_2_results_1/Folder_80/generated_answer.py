def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[14]
    prime_list = []
    for num in range(x, 0, -1):
        if is_prime(num):
            trunc = [num]
            while len(trunc[-1]) > 2:
                trunc.append(int(trunc[-1][1:-1]))
                if not is_prime(trunc[-1]):
                    break
            else:
                prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list