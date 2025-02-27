def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n):
    final_list = []
    for i in range(2, n + 1):
        if '0' in str(i):
            continue
        while i > 1:
            if i / 10 < 1:
                final_list.append(i)
                break
            else:
                i = i % (10 ** len(str(i)) - 10 ** (len(str(i)) - 1))
                if i / 10 > 1:
                    i = i / 10
    final_list = [i for i in final_list if is_prime(i)]
    return sorted(final_list)