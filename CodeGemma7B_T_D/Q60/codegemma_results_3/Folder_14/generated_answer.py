def all_left_right_truncatable_prime(tuple):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result_list = []
    for x in prime_list:
        flag = True
        for digit in str(x):
            if digit == '0':
                flag = False
                break
            if not is_prime(x):
                flag = False
                break
        if flag:
            result_list.append(x)
    return sorted(result_list, reverse=True)

def is_prime(x):
    if x in [0, 1]:
        return False
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            return False
    return True