def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    results = []
    for i in range(x - 1, 1, -1):
        str_i = str(i)
        if str_i[-1] == '0':
            continue
        while len(str_i) > 1:
            if not is_prime(int(str_i)):
                break
            str_i = str_i[1:]
        if is_prime(int(str_i)):
            results.append(i)
    return sorted(results, reverse=True)