def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[630]
    result_list = []
    for i in range(x, 0, -1):
        if is_prime(i):
            a = i
            while a:
                if not is_prime(a):
                    break
                a //= 10
            else:
                result_list.append(i)
    result_list.sort(reverse=True)
    return result_list