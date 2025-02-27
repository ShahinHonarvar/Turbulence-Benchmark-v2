def all_right_truncatable_prime(num):
    """
    Write a function called 'all_right_truncatable_prime' that takes an argument which is a tuple of positive integers. Let x be the integer at index 35. The function should return the sorted list of all right-truncatable prime numbers less than x. The returned list should be sorted in descending order. If there is no such right-truncatable prime number, the function should return an empty list. A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
    """
    temp = list(num)
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    result = []
    for i in range(len(temp)):
        if int(''.join(temp[i:])) in prime:
            result.append(int(''.join(temp[i:])))
    for i in range(len(temp)):
        del temp[i]
        if int(''.join(temp)) in prime:
            result.append(int(''.join(temp)))
    result.sort()
    result.reverse()
    return result