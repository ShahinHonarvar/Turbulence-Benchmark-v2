def all_left_truncatable_prime(n):
    n.sort()
    lst = []
    idx = -1
    cnt = 0
    for idx in range(len(n)):
        while cnt < idx and n[idx] % 10 != 0:
            cnt += 1
        if n[idx] % 10 == 0:
            if is_prime(n[idx]):
                lst.append(n[idx])
        else:
            if is_prime(n[idx]):
                lst.append(n[idx])
            cnt += 1
    return lst

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True