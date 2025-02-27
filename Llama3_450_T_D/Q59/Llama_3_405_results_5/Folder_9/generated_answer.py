def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[29]

    def is_left_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    return sorted([n for n in range(11, x) if '0' not in str(n) and is_prime(n) and is_left_truncatable_prime(n)], reverse=True)