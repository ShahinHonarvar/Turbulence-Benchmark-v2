def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(tpl):
    x = tpl[36]
    res = []
    for i in range(2, x):
        if is_prime(i):
            if i % 10 != 0 and is_prime(i // 10):
                j = i
                while j > 9:
                    if not is_prime(j // 10):
                        break
                    j = j // 10
                else:
                    res.append(i)
    return sorted(res)