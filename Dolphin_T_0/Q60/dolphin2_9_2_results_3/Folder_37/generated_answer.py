def all_left_right_truncatable_prime(arg):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) == 0 or not is_prime(int(str_n[i:])):
                return False
            if int(str_n[:i]) == 0 or not is_prime(int(str_n[:i])):
                return False
        return True
    x = arg[35]
    result_list = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result_list, reverse=True)