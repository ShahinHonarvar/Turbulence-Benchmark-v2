def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[39]
    result = [2]
    for i in range(3, x):
        if is_prime(i):
            i_str = str(i)
            if '0' not in i_str:
                for j in range(len(i_str) - 1):
                    if not is_prime(int(i_str[j:])):
                        break
                else:
                    result.append(i)
    return result