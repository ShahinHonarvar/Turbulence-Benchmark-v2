def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers_tuple[96]
    prime_numbers = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            while str_num:
                if not is_prime(int(str_num)):
                    break
                str_num = str_num[1:-1]
                if str_num:
                    if not is_prime(int(str_num)):
                        break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)