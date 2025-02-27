def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[78]
    result = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        s = str(i)
        if '0' in s:
            continue
        for j in range(1, len(s)):
            if not is_prime(int(s[j:])):
                break
        else:
            for k in range(len(s) - 1):
                if not is_prime(int(s[:-k - 1])):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)