def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(lst):
    x = lst[84]
    result = []
    for i in range(x, 0, -1):
        s = str(i)
        if s[0] != '0':
            if is_prime(i):
                is_trunc_prime = True
                for j in range(1, len(s)):
                    if not is_prime(int(s[j:])):
                        is_trunc_prime = False
                        break
                if is_trunc_prime:
                    result.append(i)
    return result