def all_left_truncatable_prime(tuple_number):
    x = tuple_number[992]
    left_truncatable_prime = []
    for number in range(x):
        temp = number
        number_list = []
        while temp > 0:
            x = temp % 10
            temp = int(temp / 10)
            number_list.append(x)
        number_list.reverse()
        number_str = ''
        for item in number_list:
            number_str += str(item)
        number = int(number_str)
        if number > 2:
            flag = True
            for i in range(3, int(number ** 0.5) + 1):
                if number % i == 0:
                    flag = False
                    break
            if flag:
                prime_number_list = [str(number)]
                for i in range(len(str(number)) - 1):
                    temp = number_str[i + 1:]
                    temp_number = int(temp)
                    prime_flag = True
                    for j in range(3, int(temp_number ** 0.5) + 1):
                        if temp_number % j == 0:
                            prime_flag = False
                            break
                    if prime_flag:
                        prime_number_list.append(temp)
                if len(prime_number_list) == len(str(number)):
                    left_truncatable_prime.append(prime_number_list[0])
    left_truncatable_prime.sort()
    return left_truncatable_prime