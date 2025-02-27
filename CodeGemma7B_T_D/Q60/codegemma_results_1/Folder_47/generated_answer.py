def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for k in range(2, x + 1):
        if len(str(k)) > 1 and '0' not in str(k) and is_prime(k):
            n = k
            flag = True
            while n > 1:
                if not is_prime(n):
                    flag = False
                    break
                n = int(str(n)[:-1])
            if flag:
                n = k
                flag = True
                while n > 1:
                    if not is_prime(n):
                        flag = False
                        break
                    try:
                        n = int(str(n)[1:])
                    except:
                        n = int(str(n)[:-1])
                if flag:
                    result.append(k)
    return sorted(result)