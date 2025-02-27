def decimal_divisible_by_fibonacci_54th(number_binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_bin_value(number_binary):
        list_binary = list(number_binary)
        list_binary.reverse()
        decimal_value = 0
        for i in range(len(list_binary)):
            decimal_value += int(list_binary[i]) * 2 ** i
        return decimal_value

    def update_index_fibonacci_number(decimal_value):
        fibonacci_number = fibonacci(index_fibonacci_number)
        while fibonacci_number < decimal_value:
            index_fibonacci_number += 1
            fibonacci_number = fibonacci(index_fibonacci_number)
        return fibonacci_number
    index_fibonacci_number = 0
    if number_binary == '1':
        return True
    else:
        decimal_value = get_bin_value(number_binary)
        fibonacci_number = update_index_fibonacci_number(decimal_value)
        return fibonacci_number % decimal_value == 0