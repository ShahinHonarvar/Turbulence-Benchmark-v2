def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[79]
    lst = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            num = i
            while num > 0:
                num = int(str(num)[1:])
                if num < 2 or not is_prime(num):
                    break
            else:
                num = i
                while num > 0:
                    num = int(str(num)[:-1])
                    if num < 2 or not is_prime(num):
                        break
                else:
                    lst.append(i)
    return sorted(lst, reverse=True)