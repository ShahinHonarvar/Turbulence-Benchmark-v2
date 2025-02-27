def all_left_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    x = tuple_of_positive_integers[24]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        temp = str_num
        while len(temp) > 1:
            if not is_prime(int(temp)):
                break
            temp = temp[1:-1]
        else:
            primes.append(num)
    return sorted(primes)