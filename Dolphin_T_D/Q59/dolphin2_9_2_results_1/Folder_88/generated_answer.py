def all_left_truncatable_prime(n):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    x = n[93]
    res = [x]
    i = x - 1
    while i >= 2:
        if is_prime(i):
            if len(res) == 0:
                res.append(i)
            else:
                for j in str(i):
                    if i != int(j):
                        left = i
                        for k in str(res[-1]):
                            if left == int(k):
                                res.append(i)
                                break
                            else:
                                left = int(''.join([str(k), str(left)]))
                    else:
                        break
        i -= 1
    return sorted(res)