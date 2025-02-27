def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[92]
    result = []
    for num in range(10, x):
        str_num = str(num)
        is_truncatable_prime = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(num)
    return sorted(result)