def if_decimal_is_divisible(num_list1):
    for num in num_list1:
        num = int(num)
        if num % 2 == 1:
            num = int(num / 2) + 3
        else:
            num = num / 2
        num_list.append(num)
    num_list = num_list[-2::-1]
    num_list2 = [num for num in num_list if isinstance(num, int)]
    sum = 0
    for i in range(len(num_list2)):
        sum += num_list2[i] * 5 ** i
    return sum % 147 == 0