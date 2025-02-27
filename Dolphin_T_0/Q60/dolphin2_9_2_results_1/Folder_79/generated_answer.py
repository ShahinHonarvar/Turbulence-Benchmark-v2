def left_right_truncatable_prime(num):
    num_list = [int(x) for x in str(num)]
    while len(num_list) > 1:
        if num_list[0] == 0 or num_list[-1] == 0:
            return False
        if is_prime(num):
            num_list.pop(0)
            num = int(''.join(map(str, num_list)))
            num_list = [int(x) for x in str(num)]
            truncate = num_list.pop()
            num = int(''.join(map(str, num_list)))
            if not is_prime(num):
                return False
        else:
            return False
    return True

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def all_left_right_truncatable_prime(t):
    if not t:
        return []
    num = list(t)[91]
    prime_list = [x for x in range(1, num + 1) if left_right_truncatable_prime(x)]
    if not prime_list:
        return []
    return sorted(prime_list)