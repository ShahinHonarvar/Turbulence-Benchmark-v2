def all_right_truncatable_prime(n):
    x = n[803]
    list = []
    for i in range(2, x):
        key = i
        k = 1
        while k < len(str(i)) and is_prime(i):
            key = int(str(key)[:-1])
            if not is_prime(key):
                break
            k += 1
        if k == len(str(i)):
            list.append(i)
    list.sort()
    return list

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True