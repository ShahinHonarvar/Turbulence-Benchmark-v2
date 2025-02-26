def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not (is_prime(int(str_num)) and str_num.find('0') == -1):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            left = num
            right = num
            while len(str(left)) > 1:
                left //= 10
                if not is_prime(left):
                    is_truncatable = False
                    break
            while len(str(right)) > 1:
                right %= 10 ** (len(str(right)) - 1)
                if not is_prime(right):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)