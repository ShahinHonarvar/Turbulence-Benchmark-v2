def all_right_truncatable_prime(maxval):
    res = []
    for i in range(2, maxval):
        j = i
        is_prime = True
        while j != 0 and is_prime:
            if j in [0, 1]:
                is_prime = False
            elif j in [2, 3, 5, 7]:
                is_prime = True
            elif j % 2 == 0 or j % 3 == 0 or j % 5 == 0 or (j % 7 == 0):
                is_prime = False
            else:
                is_prime = True
            j //= 10
        if is_prime:
            while j != 0:
                if j % 2 == 0 or j % 3 == 0 or j % 5 == 0 or (j % 7 == 0):
                    is_prime = False
                    break
                j //= 10
            if is_prime:
                res.append(i)
    res.sort()
    return res or []