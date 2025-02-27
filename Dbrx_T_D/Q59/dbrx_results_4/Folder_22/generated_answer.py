def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    digits = list(str(n))
    for i in range(len(digits)):
        if int(''.join(digits[i:])) < 10:
            break
        if not is_prime(int(''.join(digits[i:]))):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[85]
    lst = [i for i in range(10, x) if left_truncatable_prime(i)]
    return sorted(lst)