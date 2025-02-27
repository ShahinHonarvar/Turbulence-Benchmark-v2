def all_left_truncatable_prime(num):
    x = num[26]
    ans = []
    i = x - 1
    while i > 1:
        if isprime(i) and lefttruncatableprime(i):
            ans.append(i)
        i -= 1
    return sorted(ans)

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def lefttruncatableprime(num):
    numstr = str(num)
    for i in range(len(numstr)):
        if numstr.startswith('0') or not isprime(int(numstr[i:])):
            return False
    return True