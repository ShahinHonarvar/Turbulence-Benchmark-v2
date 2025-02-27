def all_left_right_truncatable_prime(x):
    """
    A function that takes a tuple of positive integers as an argument, 
    and returns a list of all left-and-right-truncatable prime numbers less than or equal to x,
    sorted in descending order. If no such primes exist in the range, an empty list is returned.
    """
    result = []
    for num in range(2, x + 1):
        trunc_num = str(num)
        while trunc_num and trunc_num[-1] == '0':
            trunc_num = trunc_num[1:-1]
        while trunc_num and trunc_num[0] == '0':
            trunc_num = trunc_num[1:]
        if trunc_num != '' and all(trunc_num.lstrip('0').rstrip('0').isdigit()):
            if is_prime(num) and is_prime(int(trunc_num.lstrip('0').rstrip('0'))):
                result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):
    """
    A function that checks if a number is a prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True