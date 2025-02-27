def all_left_truncatable_prime(t):
    x = max(t)
    all_left_truncatable_prime_list_built = [i for i in range(2, x) if all_check_left_truncatable(i)]
    return all_left_truncatable_prime_list_built

def all_check_left_truncatable(num):
    num_str_list = list(str(num))
    for digit in num_str_list:
        if digit == '0':
            return False
    for N in range(len(num_str_list)):
        num_str_list.pop(0)
        pop_list = []
        for digit in num_str_list:
            pop_list.append(digit)
        pop_int = int(''.join(pop_list))
        if pop_int > 1:
            if not all_prime_check(pop_int):
                return False
    return True

def all_prime_check(num):
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True