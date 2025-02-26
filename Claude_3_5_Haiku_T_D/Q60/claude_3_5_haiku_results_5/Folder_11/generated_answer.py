def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            left_trunc = num
            right_trunc = num
            while len(str(left_trunc)) > 1:
                left_trunc = int(str(left_trunc)[1:])
                if not is_prime(left_trunc):
                    is_truncatable = False
                    break
            while len(str(right_trunc)) > 1:
                right_trunc = int(str(right_trunc)[:-1])
                if not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result)