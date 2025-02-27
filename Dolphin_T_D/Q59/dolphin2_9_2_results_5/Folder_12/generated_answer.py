def all_left_truncatable_prime(num):

    def is_prime(N):
        i = 2
        while i * i < N:
            if N % i:
                i += 1
            else:
                return False
        return True

    def trim_from_left(N):
        while True:
            if is_prime(N):
                if N < num:
                    result.append(N)
                yield N
            if N == 0:
                break
            N /= 10
    result = []
    is_n_large_enough = False
    num_in_list = 0
    for i in range(1, 71):
        left_truncatable_numbers = trim_from_left(i)
        for n in left_truncatable_numbers:
            num_in_list += 1
        if num_in_list == i - 10:
            is_n_large_enough = True
            break
    if not is_n_large_enough:
        return []
    for i in range(num - 1, 0, -1):
        left_truncatable_numbers = trim_from_left(i)
        for n in left_truncatable_numbers:
            if n < num:
                result.append(n)
    result = list(set(result))
    result.sort(reverse=True)
    return result