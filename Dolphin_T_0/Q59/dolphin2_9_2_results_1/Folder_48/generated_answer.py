def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    """Function to find all left-truncatable prime numbers less than a given number x"""
    x = t[835] - 1
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            flag = True
            for j in range(len(str_i) - 1, 0, -1):
                if len(str_i) == 1:
                    result.append(i)
                    break
                sub_str_i = str_i[:j]
                if not is_prime(int(sub_str_i)):
                    flag = False
                    break
            if flag:
                result.append(i)
    return sorted(result)