def all_right_truncatable_prime(my_tuple):
    x = my_tuple[41]
    ans = []
    for i in range(2, x):
        if isprime(i):
            j = i
            while j > 0:
                if not isprime(j):
                    break
                j = j // 10
            else:
                ans.append(i)
    return sorted(ans)

def isprime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True