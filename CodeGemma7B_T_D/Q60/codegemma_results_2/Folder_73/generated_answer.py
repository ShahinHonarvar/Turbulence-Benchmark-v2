def all_left_right_truncatable_prime(n):
    """
    :type n: tuple[int]
    :rtype: list[int]
    """
    n = n[96]
    if n < 2 or n % 2 == 0:
        return []
    result = []
    for m in range(n + 1):
        if is_truncatable_prime(m):
            result.append(m)
    if not result:
        return []
    return sorted(result)

def is_truncatable_prime(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 2 or n % 2 == 0:
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    n = max(int(str_n[0]), int(str_n[-1]))
    for i in range(len(str_n)):
        digit = int(str_n[i])
        if digit != n:
            continue
        if not is_prime(n):
            return False
        str_n = str_n[0:i] + str_n[i + 1:]
    return True

def is_prime(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True