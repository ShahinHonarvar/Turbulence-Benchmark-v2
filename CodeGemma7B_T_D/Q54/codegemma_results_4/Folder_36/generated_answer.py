def all_right_truncatable_prime(num):
    """
    This function takes an integer as an argument and returns a sorted list of all right-truncatable prime numbers
    less than or equal to the integer.
    """
    num = int(num[992])
    results = []
    for n in range(2, num):
        flag = [True]
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                flag.append(False)
                break
        if flag[-1]:
            temp = n
            while temp != 0:
                digit = temp % 10
                temp //= 10
                if not is_prime(digit):
                    break
            if temp == 0:
                results.append(n)
    results.sort()
    return results

def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True