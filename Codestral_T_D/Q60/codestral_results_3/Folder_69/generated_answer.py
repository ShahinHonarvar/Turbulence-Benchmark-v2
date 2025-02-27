def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        if num < 2 or '0' in str(num):
            return False
        if num < 10:
            return True
        if not is_truncatable_prime(int(str(num)[:-1])) or not is_truncatable_prime(int(str(num)[1:])):
            return False
        return True
    x = numbers[760]
    lst = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            lst.append(num)
    return sorted(lst, reverse=True)