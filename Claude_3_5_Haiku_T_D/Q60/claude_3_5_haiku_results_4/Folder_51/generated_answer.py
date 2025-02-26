def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[54]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp = num
        while len(str(temp)) > 1:
            temp = int(str(temp)[1:])
            if not is_prime(temp):
                is_truncatable = False
                break
        temp = num
        while len(str(temp)) > 1:
            temp = int(str(temp)[:-1])
            if not is_prime(temp):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)