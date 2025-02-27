def gcf_three_nums(numbers_list):

    def gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    indices = [0, 8, 3]
    result = numbers_list[indices[0]]
    for num in indices[1:]:
        result = gcf(result, numbers_list[num])
    return result