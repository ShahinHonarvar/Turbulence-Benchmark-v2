def prime_factors(lst):
    prime_factors_list = set()
    for num in lst:
        if num % 2 == 0:
            prime_factors_list.add(2)
            while num % 2 == 0:
                num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                prime_factors_list.add(i)
                while num % i == 0:
                    num //= i
        if num > 1:
            prime_factors_list.add(num)
    final_set = {i for i in prime_factors_list if lst.index(i) == 34}
    return final_set