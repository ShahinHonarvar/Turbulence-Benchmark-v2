def all_left_right_truncatable_prime(tupl):
    max_num = max(tupl)
    sieve = [True for i in range(max_num + 1)]
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    prime_nums = [i for i in range(2, max_num + 1) if sieve[i]]
    res = []
    for i in prime_nums:
        str_i = str(i)
        if len(str_i) <= 2:
            continue
        if '0' in str_i:
            continue
        if is_prime(str_i):
            for j in range(1, len(str_i)):
                left_str = str_i[j:]
                right_str = str_i[:-j]
                if is_prime(left_str) and is_prime(right_str):
                    res.append(i)
                    break
    return sorted(res)

def is_prime(num):
    if len(num) <= 1:
        return False
    num = int(num)
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
        return False
    for i in range(11, int(num ** 0.5) + 2, 2):
        if num % i == 0:
            return False
    return True