from syntactic.special_numbers import is_prime

def all_left_truncatable_prime(args: tuple) -> list:
    x = args[177]
    result = []
    for num in range(1, x):
        str_num = str(num)
        if str_num.startswith('0'):
            continue
        is_left_truncatable_prime = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            result.append(num)
    return result