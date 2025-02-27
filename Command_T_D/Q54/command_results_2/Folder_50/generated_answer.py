import itertools

def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: is_right_truncatable_prime(x), range(2, n[57] + 1))), reverse=True)

def is_right_truncatable_prime(n):
    if n < 10:
        return True
    if n % 2 == 0 or n % 5 == 0:
        return False
    if len(str(n)) == 1:
        return True
    if len(str(n)) == 2:
        if str(n)[-1] not in '1379':
            return False
        return True
    for d in str(n):
        if d not in '1379':
            return False
    return True