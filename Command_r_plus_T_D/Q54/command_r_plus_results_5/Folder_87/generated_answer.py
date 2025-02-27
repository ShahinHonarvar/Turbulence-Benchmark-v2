def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    str_num = str(num)
    return [int(str_num[:i]) for i in range(len(str_num), 0, -1)]

def all_right_truncatable_prime(numbers):
    limit = numbers[39]
    prime_list = []
    for num in range(limit, 0, -1):
        if is_prime(num):
            trunc_list = right_truncate(num)
            if all((is_prime(i) for i in trunc_list)):
                prime_list.append(num)
    return sorted(prime_list, reverse=True)