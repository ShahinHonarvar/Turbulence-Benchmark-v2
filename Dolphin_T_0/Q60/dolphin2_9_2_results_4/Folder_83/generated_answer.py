def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tup):
    nums = []
    x = num_tup[24]
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        else:
            r = int(str(i)[-1])
            l = int(str(i)[0])
            if is_prime(i) and is_prime(int(str(i)[1:-1])) and (l != 0 or r != 0):
                nums.append(i)
    return nums