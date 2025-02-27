def if_perfect_num(numbers):

    def if_perfect_number(num):
        return sum([i for i in range(1, num) if num % i == 0]) == num
    return if_perfect_number(numbers[194]) if len(numbers) > 194 else False