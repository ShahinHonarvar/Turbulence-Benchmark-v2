def all_left_truncatable_prime(tupl):
    list_of_prime = []
    for num in tupl:
        if not (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i != 0:
                    str_num = str(num)
                    is_prime = True
                    for j in range(1, len(str_num)):
                        if int(str_num[j:]) % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        list_of_prime.append(num)
    list_of_prime.sort(reverse=True)
    return list_of_prime