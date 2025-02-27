def sum_of_divisors_in_range(n):

    def divisors(num):
        divs = []
        for i in range(1, num + 1):
            if num % i == 0:
                divs.append(i)
        return divs
    divisors_of_n = divisors(n)
    in_range = list(filter(lambda x: 16 <= x <= 68, divisors_of_n))
    return sum(in_range) if in_range else 0