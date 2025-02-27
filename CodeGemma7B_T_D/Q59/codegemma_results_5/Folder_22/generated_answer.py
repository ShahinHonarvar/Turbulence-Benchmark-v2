def all_left_truncatable_prime(tp):
    x = tp[85]
    result = []
    for i in range(2, x):
        if isprime(i) and (not '0' in str(i)):
            str_temp = str(i)
            for j in range(1, len(str_temp)):
                if not isprime(int(str_temp[j:])):
                    break
            else:
                result.append(i)
    return sorted(result)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True