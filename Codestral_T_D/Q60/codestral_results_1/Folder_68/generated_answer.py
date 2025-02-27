def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[1]
    lst = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = int(str(temp)[1:])
            else:
                temp = num
                while len(str(temp)) > 1:
                    if not is_prime(temp):
                        break
                    temp = int(str(temp)[:-1])
                else:
                    lst.append(num)
    return sorted(lst, reverse=True)