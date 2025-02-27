def find_primes_between_indices(number_list):
    prime = []
    for number in number_list[52:54]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime.append(number)
    prime.sort()
    return prime