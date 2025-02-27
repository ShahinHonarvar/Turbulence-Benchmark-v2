def all_right_truncatable_prime(tup):

    def is_prime(num):
        if num < 2:
            return False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
    x = tup[85]
    prime = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1, 0, -1):
                if not is_prime(int(str_num[i:])):
                    break
                if i == 1:
                    prime.append(num)
    return sorted(prime)