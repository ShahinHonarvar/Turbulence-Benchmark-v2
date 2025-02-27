def all_left_truncatable_prime(n):
    all_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    answer = []
    for i in n:
        if i in all_primes:
            copy_i = i
            maximum = int(str(i)[0])
            while copy_i != 0:
                i = copy_i
                copy_i //= 10
                if int(str(i)[0]) > maximum:
                    maximum = int(str(i)[0])
                    t = 0
                    while t <= maximum - int(str(i)[0]):
                        t += 1
                        if t in all_primes:
                            answer.append(i)
                            break
    answer.sort(reverse=True)
    return answer