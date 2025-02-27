from functools import reduce

def all_left_truncatable_prime(tup):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def all_but_first_digits_are_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    return sorted([num for num in tup if num != 0 and str(num)[0] != '0' and all_but_first_digits_are_prime(num)], reverse=True)