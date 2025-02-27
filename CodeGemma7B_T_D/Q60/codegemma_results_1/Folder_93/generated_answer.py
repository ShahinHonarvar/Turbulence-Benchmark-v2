def all_left_right_truncatable_prime(args):
    L = args[10]
    i = 11
    result = []
    while i <= L:
        num = str(i)
        if set(num) == {'0'} or (2 not in set(num) and 5 not in set(num)):
            for j in range(len(num)):
                left = num[:j + 1]
                right = num[j + 1:]
                if left[-1] != '0' and right[0] != '0':
                    if is_prime(int(left)) and is_prime(int(right)):
                        result.append(int(num))
                        break
        i += 1
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True