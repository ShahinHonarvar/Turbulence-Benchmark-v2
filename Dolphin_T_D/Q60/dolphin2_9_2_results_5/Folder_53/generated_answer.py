def all_left_right_truncatable_prime(x):
    """Return a list of all left-and-right-truncatable prime numbers less than or equal to x"""
    left_right_primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            new_num = num
            while len(new_num) > 1:
                new_num = new_num[1:-1]
                if new_num[0] == '0' or all((new_num % i != 0 for i in range(2, int(new_num ** 0.5) + 1))):
                    left_right_primes.append(int(new_num))
            if int(new_num[1]) != 0:
                left_right_primes.append(int(new_num[1]))
    return sorted(left_right_primes, reverse=True)