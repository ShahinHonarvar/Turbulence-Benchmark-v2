def all_right_truncatable_prime(tu):
    answer = [2, 3, 5, 7]
    ar = [2, 3, 5, 7]
    x = tu[28]
    fl = 0
    for i in range(2, x):
        if ar[-1] + 2 >= i >= ar[-1]:
            if is_prime(i):
                if is_truncatable_prime(i):
                    ar.append(i)
                    answer.append(i)
        elif ar[-1] + 1 >= i >= ar[-1]:
            if is_prime(i):
                ar.append(i)
    if len(answer) == 4:
        return []
    answer.sort()
    return answer

def is_truncatable_prime(i):
    ok = 0
    answer = list(str(i))
    for j in range(1, len(answer)):
        del answer[-1]
        if not is_prime(int(''.join(answer))):
            break
        else:
            ok = 1
    if ok == 1:
        return True
    else:
        return False

def is_prime(n):
    fl = 0
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            fl = 1
            break
    if fl == 1:
        return False
    else:
        return True