def sum_of_divisors_in_range(n):

    def divisors(num):
        divs = []
        for i in range(1, num + 1):
            if num % i == 0:
                divs.append(i)
        return divs
    divs_in_range = [div for div in divisors(n) if 111 <= div <= 508]
    return sum(divs_in_range) if divs_in_range else 0