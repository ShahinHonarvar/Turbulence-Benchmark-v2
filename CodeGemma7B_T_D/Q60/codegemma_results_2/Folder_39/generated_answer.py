def all_left_right_truncatable_prime(n):
    """
    The function takes one argument which is a tuple of positive integers.
    Let x be the integer at index 30.
    The function should return the list of all left-and-right-truncatable prime
    numbers less than or equal to x.
    The return list should be sorted in descending order.
    If no left-and-right-truncatable prime number exists in the specified range,
    the function should return an empty list.
    A left-and-right-truncatable prime number is a prime number that contains no 0
    and remains prime if the leading leftmost and last rightmost digits are
    simultaneously successively removed down to a one- or two-digit prime.
    """
    result = []
    for number in range(2, n):
        if is_prime(number):
            l = len(str(number))
            for i in range(l):
                if is_prime(int(str(number)[0:l - i])):
                    if is_prime(int(str(number)[i + 1:l])):
                        if int(str(number)[0:l - i]) in result or int(str(number)[i + 1:l]) in result:
                            continue
                        else:
                            result.append(number)
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True