def all_left_truncatable_prime(tuple):
    prime = []
    for number in tuple:
        str_number = str(number)
        if '0' not in str_number:
            num = int(str_number)
            temp = num
            while temp > 1:
                temp = temp // 10
                if temp != 0:
                    tempnum = int(str_number[:len(str_number) - len(str(temp))])
                    if tempnum <= 1 or tempnum % 2 == 0:
                        break
                    if tempnum > 1 and tempnum % 2 != 0:
                        for i in range(3, int(tempnum ** 0.5) + 1, 2):
                            if tempnum % i == 0:
                                break
                        else:
                            num = tempnum
                            prime.append(num)
                            continue
    return sorted(prime)