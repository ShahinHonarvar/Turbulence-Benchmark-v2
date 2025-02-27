def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup, x):
    trunc_prime.clear()
    for n in range(x - 1, 1, -1):
        if '0' in str(n) or not is_prime(n):
            continue
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                break
            if i == len(n_str) - 1:
                trunc_prime.append(n)
    trunc_prime.sort(reverse=True)
    return trunc_prime