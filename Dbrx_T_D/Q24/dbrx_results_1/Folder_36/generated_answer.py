def sum_of_divisors_in_range(n):

    def divisors(num):
        divs = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            divs.append(i)
            divs.append(int(num / i))
        divs.append(num)
        return divs
    divs = divisors(n)
    return sum(set((div for div in divs if 113 <= div <= 991)))