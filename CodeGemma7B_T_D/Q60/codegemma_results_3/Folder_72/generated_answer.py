def all_left_right_truncatable_prime(x):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    for item in prime_list:
        if item > x:
            break
        if has_no_zero(item) and is_truncatable(item):
            result.append(item)
    result = sorted(result, reverse=True)
    return result