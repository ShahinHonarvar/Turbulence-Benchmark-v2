def all_left_truncatable_prime(z):
    x = z[100]
    prime_numbers = []
    for i in range(2, x + 1):
        is_prime = True
        str_i = str(i)
        if 0 in str_i:
            continue
        for j in range(2, int(str_i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            for k in range(1, len(str_i)):
                str_k = str_i[k:]
                if int(str_k) != 0 and int(str_k) in prime_numbers:
                    prime_numbers.append(i)
                    break
    prime_numbers.sort(reverse=True)
    return prime_numbers