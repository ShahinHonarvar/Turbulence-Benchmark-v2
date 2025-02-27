def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    ans = []
    for prime in primes:
        s = str(prime)
        if '0' in s:
            continue
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                break
        else:
            ans.append(prime)
    ans.sort(reverse=True)
    return ans