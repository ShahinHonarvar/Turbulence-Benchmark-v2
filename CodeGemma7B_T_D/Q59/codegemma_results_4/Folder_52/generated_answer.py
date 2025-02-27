def all_left_truncatable_prime(t):
    x = t[52]
    prime = []
    for i in range(2, x + 1):
        if is_prime(i):
            if check_left_trunc(i):
                prime.append(i)
    prime.sort(reverse=True)
    return prime

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def check_left_trunc(x):
    str_x = str(x)
    if '0' in str_x:
        return False
    for i in range(1, len(str_x)):
        if not is_prime(int(str_x[i:])):
            return False
    return True