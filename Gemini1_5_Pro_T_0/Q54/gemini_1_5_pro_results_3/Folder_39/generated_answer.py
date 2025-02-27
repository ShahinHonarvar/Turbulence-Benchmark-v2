def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable_prime = True
        str_num = str(num)
        for i in range(len(str_num) - 1, 0, -1):
            if int(str_num[:i]) not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] or int(str_num[:i]) == 1:
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime and num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes