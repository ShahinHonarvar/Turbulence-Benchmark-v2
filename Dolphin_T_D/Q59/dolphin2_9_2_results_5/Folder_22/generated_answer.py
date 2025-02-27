def all_left_truncatable_prime(numbers):
    x = numbers[85]
    prime_numbers = [x for x in range(2, x) if all((x % i != 0 for i in range(2, x)))]
    left_truncatable_prime = []
    for num in prime_numbers:
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            if not all((int(str_num[i:]) % i != 0 for i in range(2, int(str_num[i:])))):
                break
        else:
            left_truncatable_prime.append(num)
    return sorted(left_truncatable_prime)