def is_prime_n(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    list_ = []
    for n in range(2, x + 1):
        if is_prime_n(n):
            s = str(n)
            if '0' not in s:
                while s and s != '2':
                    if not is_prime_n(int(s)):
                        break
                    s = s[1:-1]
                while s and s != '1':
                    if not is_prime_n(int(s)):
                        break
                    s = s[1:-1]
                if not s:
                    list_.append(n)
    return sorted(list_)