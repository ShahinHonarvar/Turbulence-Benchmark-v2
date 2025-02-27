def all_left_right_truncatable_prime(t):
    x = t[93]
    lst = []
    for i in range(2, x + 1):
        if isprime(i):
            if is_truncatable_prime(i):
                lst.append(int(str(i)))
    return sorted(lst)

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    return all((isprime(int(n_str[0:len(n_str) - i])) and isprime(int(n_str[i:len(n_str)])) for i in range(1, len(n_str))))