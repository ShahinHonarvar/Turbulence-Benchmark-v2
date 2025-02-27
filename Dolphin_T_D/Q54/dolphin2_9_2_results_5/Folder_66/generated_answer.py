def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[25]
    ans = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            k = i
            while k > 1:
                k = int(k / 10)
                if not is_prime(k):
                    break
            else:
                ans.append(i)
    return sorted(ans, reverse=True)