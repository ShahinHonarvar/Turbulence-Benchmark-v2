def all_left_truncatable_prime(tup):
    x = tup[7]
    prime_list = [2, 3, 5, 7]
    result = []
    for i in range(2, x):
        if all((digit not in str(i) for digit in '0')):
            truncate_i = i
            while truncate_i > 0:
                if truncate_i not in prime_list:
                    break
                truncate_i //= 10
            else:
                prime_list.append(i)
                result.append(i)
    return sorted(result)