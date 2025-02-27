def all_even_ints_inclusive(int_list):
    answer = []
    for i in range(82, 87):
        if int_list[i] % 2 == 0:
            answer.append(int_list[i])
    if not answer:
        return []
    return answer