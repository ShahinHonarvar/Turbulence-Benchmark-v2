def if_decimal_is_divisible(binary_representaion):
    fibonacci_74 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
    final_list = []
    binary_representaion_list = list(binary_representaion)
    reversed_list = binary_representaion_list[::-1]
    for i in range(len(reversed_list)):
        if reversed_list[i] == '1':
            final_list.append(2 ** i)
    final_list = list(map(int, final_list))
    final_decimal = 0
    for i in range(len(final_list)):
        if final_list[i] > fibonacci_74[i]:
            break
        else:
            final_decimal += final_list[i] * fibonacci_74[i]
    if final_decimal % fibonacci_74[-1] == 0:
        return True
    else:
        return False