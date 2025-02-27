def all_left_truncatable_prime(tup):

    def is_left_truncatable_prime(num):
        num = str(num)
        while len(num) > 1:
            if not is_prime(num):
                return False
            num = num[1:]
        return True

    def is_prime(num):
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num == 1:
            return False
        i = 3
        while i * i <= num:
            if num % i:
                i += 2
            else:
                return False
        return True
    x = tup[71]
    list_prime = [i for i in range(2, x) if is_prime(i)]
    list_trunc = [i for i in list_prime if is_left_truncatable_prime(i)]
    return sorted(list_trunc, reverse=True)