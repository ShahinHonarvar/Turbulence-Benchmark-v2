def all_left_right_truncatable_prime(x):
    """
    This function returns the list of all left- and right-truncatable prime numbers less than or equal to x.
    """
    ans = []
    if not is_prime(x):
        return ans
    for i in range(len(str(x))):
        if is_prime(int(str(x)[:i + 1])) and is_prime(int(str(x)[-i - 1::-1])):
            ans.append(int(str(x)[:i + 1]))
    return sorted(ans, reverse=True)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True