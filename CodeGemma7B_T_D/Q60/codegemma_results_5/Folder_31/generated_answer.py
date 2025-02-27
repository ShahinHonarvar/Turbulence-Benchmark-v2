def all_left_right_truncatable_prime(x):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    for i in range(0, 54):
        temp_list = []
        num = prime[i]
        while num < x:
            if num not in result and str(num) not in ['0', '2', '4', '5', '6', '8']:
                flag = True
                for j in range(2, num):
                    if num % j == 0:
                        flag = False
                        break
                if flag:
                    temp_list.append(num)
            num += 2
        if temp_list:
            temp_list.sort(reverse=True)
            result.extend(temp_list)
    return result