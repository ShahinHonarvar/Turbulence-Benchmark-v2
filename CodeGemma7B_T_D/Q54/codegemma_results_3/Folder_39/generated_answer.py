def all_right_truncatable_prime(n):
    result = []
    if len(n) <= 30:
        num = int(''.join((str(x) for x in n)))
        if is_prime(num):
            for i in range(len(n)):
                if is_prime(int(''.join((str(x) for x in n[i:])))):
                    result.append(num)
    return sorted(result, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True