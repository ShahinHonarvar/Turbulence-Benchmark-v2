def all_left_right_truncatable_prime(numbers_tuple):
    """A function that returns a list of all left-and-right-truncatable prime numbers less than or equal to a specific x"""

    def is_prime(n):
        """A helper function that evaluates if a number is prime or not"""
        if n <= 1:
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
    x = numbers_tuple[100]
    left_right_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        copy_num = num
        while copy_num > 9:
            if not is_prime(copy_num):
                break
            copy_num = int(str_num[1:-1])
            if is_prime(int(str(copy_num))):
                left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)