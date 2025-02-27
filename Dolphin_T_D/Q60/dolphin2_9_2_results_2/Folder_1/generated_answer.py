def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[20]
    ret = []
    for i in range(x, 1, -1):
        if is_prime(i):
            if '0' not in str(i):
                temp = i
                while temp != 0 and temp != 1 and (temp != 2) and (temp != 3) and (temp != 4) and (temp != 5) and (temp != 6):
                    if not is_prime(int(str(temp)[1:-1])):
                        break
                    temp = int(str(temp)[1:-1])
                if temp == 0 or temp == 1 or temp == 2 or (temp == 3) or (temp == 4) or (temp == 5) or (temp == 6):
                    ret.append(i)
    return sorted(ret, reverse=True)