def all_left_right_truncatable_prime(x):
    """Write a function called 'all_left_right_truncatable_prime' that takes one argument which is a tuple of positive integers. Let x be the integer at index 0. 
The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x. 
The return list should be sorted in descending order. 
If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
A left-and-right-truncatable prime number is a prime number that contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime."""

    def is_prime(n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def is_truncatable_prime(n):
        if n % 10 == 0 or n < 2:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result