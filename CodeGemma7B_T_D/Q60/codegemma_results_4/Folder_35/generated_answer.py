def all_left_right_truncatable_prime(tup):
    """
    Let x be the integer at index 177.
    The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in ascending order.
    If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
    """
    x = tup[177]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num) - 1):
            left = int(str_num[i:])
            right = int(str_num[:len(str_num) - i])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            result.append(i)
    return sorted(result)