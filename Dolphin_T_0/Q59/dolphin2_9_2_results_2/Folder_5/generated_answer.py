def all_left_truncatable_prime(x):

    def is_prime(n):
        """Check whether a number n is prime or not"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        to_check = num
        while to_check:
            if not is_prime(to_check):
                break
            str_to_check = str(to_check)
            to_check = int(str_to_check[1:])
        if to_check == 0:
            result.append(num)
    return sorted(result)