def all_left_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x_tuple[54]
    prompts = [2, 3, 5, 7]
    i = 0
    while prompts[i] < x:
        str_num = str(prompts[i])
        if all((is_prime(int(str_num[j:])) for j in range(len(str_num)))):
            prompts.append(prompts[i])
        i += 1
    prompts = list(set(prompts))
    prompts.sort()
    return prompts