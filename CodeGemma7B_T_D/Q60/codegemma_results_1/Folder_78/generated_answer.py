def all_left_right_truncatable_prime(tupl):
    digits = set('0123456789')
    prime = lambda n: all((n % i for i in range(2, int(n ** 0.5) + 1)))
    ans = []
    x = tupl[23]
    for n in range(2, x + 1):
        a = str(n)
        if '0' in a or not prime(n):
            continue
        while len(a) >= 2 and prime(int(a)):
            a = a[1:]
        while len(a) >= 2 and prime(int(a[::-1])):
            a = a[:-1]
        if len(a) == 2 and prime(int(a)):
            ans.append(n)
    return ans