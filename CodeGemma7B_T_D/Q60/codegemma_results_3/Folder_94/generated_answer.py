def all_left_right_truncatable_prime(tup):
    x = tup[43]
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i and is_prime(int(str_i[1:])) and is_prime(int(str_i[:-1])):
                prime_list.append(i)
    prime_list.sort()
    return prime_list

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True