def right_truncatable_prime(num):
    """Return True if a number is a right-truncatable prime."""
    str_num = str(num)
    for i in range(1, len(str_num)):
        if int(str_num[:-i]) % 2 == 0 or int(str_num[:-i]) % 3 == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    """Return a list of right-truncatable prime numbers less than or equal to x."""
    x = tup[70]
    ans = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            ans.append(i)
    ans.sort(reverse=True)
    return ans