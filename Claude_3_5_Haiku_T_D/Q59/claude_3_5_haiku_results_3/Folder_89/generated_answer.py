def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tuple_input):
    x = tuple_input[97]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            str_num = str(num)
            is_left_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(num):
                result.append(num)
    return sorted(result, reverse=True)