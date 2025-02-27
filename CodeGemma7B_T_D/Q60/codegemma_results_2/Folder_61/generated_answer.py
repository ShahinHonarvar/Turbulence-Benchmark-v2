def all_left_right_truncatable_prime(num):
    prime_list = []
    for i in range(10, num + 1):
        if is_prime(i):
            prime_list.append(i)
    for i in range(100, num + 1):
        if is_prime(i):
            str_i = str(i)
            if is_prime(int(str_i[0:-1])) and is_prime(int(str_i[1:])):
                prime_list.append(i)
    for i in range(1000, num + 1):
        if is_prime(i):
            str_i = str(i)
            if is_prime(int(str_i[0:-2])) and is_prime(int(str_i[1:-1])) and is_prime(int(str_i[2:])):
                prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True