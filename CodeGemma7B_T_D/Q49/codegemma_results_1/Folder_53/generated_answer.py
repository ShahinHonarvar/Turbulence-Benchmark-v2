def if_decimal_is_divisible(number: str):

    def bit_length(n):
        if n == 0:
            return 0
        return int(math.log(n, 2)) + 1

    def calculate_binary_representation(number):
        if number == 0:
            return '0'
        result = ''
        while number > 0:
            if number % 2 == 0:
                result = '0' + result
            else:
                result = '1' + result
            number = number // 2
        return result

    def fibonacci(n):
        first_number = 0
        second_number = 1
        result_list = []
        for ii in range(n):
            first_number, second_number = (second_number, first_number + second_number)
            result_list.append(first_number)
        return result_list

    def last_binary_length_number(number: str):
        if len(number) % 64 == 63:
            return fibonacci(len(number) // 64 + 1)[-1]
        else:
            return fibonacci(len(number) // 64)[-1]
    if bit_length(int(number, 2)) >= bit_length(last_binary_length_number(number)):
        if int(number, 2) % last_binary_length_number(number) == 0:
            return True
    return False