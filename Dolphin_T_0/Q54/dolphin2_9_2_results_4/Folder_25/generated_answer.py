def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    for d in range(2, len(str(n))):
        if not is_prime(int(str(n)[-d:])):
            return False
    return True

def all_right_truncatable_prime(lst):
    x = lst[92]
    result = [i for i in range(2, x) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(result)