def all_left_truncatable_prime(arr):
    """
    arr(tuple) = (..., x)
    
    where
    x is the integer at index 37 in the tuple
    """

    def isprime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    arr = list(arr)
    x = arr[37]
    result = []
    for num in range(2, x):
        if isprime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)