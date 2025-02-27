def all_left_truncatable_prime(num_tuple):
    x = str(num_tuple[8])
    prefix_list = [x]
    for digit in x:
        prefix_list.append(digit)
    result_list = []
    for prefix in prefix_list:
        for number in itertools.permutations(prefix, len(prefix)):
            num = int(''.join(number))
            if is_prime(num) and num < int(x):
                result_list.append(num)
    result_list.sort(reverse=True)
    return result_list