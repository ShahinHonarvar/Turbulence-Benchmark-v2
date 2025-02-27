def if_decimal_is_divisible(binary_string):
    list1 = [int(binary_string[i:i + 3], 2) for i in range(0, len(binary_string), 3)]
    fibonacci_array = [0, 1]
    sum = list1[0] + list1[1]
    for i in range(2, len(list1)):
        fibonacci_array.append(sum)
        sum = fibonacci_array[-1] + fibonacci_array[-2]
    flag = False
    for i in fibonacci_array:
        if i % list1[-1] == 0:
            flag = True
    return flag