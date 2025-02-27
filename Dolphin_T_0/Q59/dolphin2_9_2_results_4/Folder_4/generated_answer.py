def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def is_left_truncatable_prime(num):
    if len(str(num)) > 1:
        if str(num)[0] != '0' and is_prime(num):
            return is_left_truncatable_prime(int(str(num)[1:]))
        else:
            return False
    else:
        return is_prime(num)

def all_left_truncatable_prime(num_tup):
    x = num_tup[96]
    prime_list = [i for i in range(x - 1, 0, -1) if is_left_truncatable_prime(i)]
    return prime_list