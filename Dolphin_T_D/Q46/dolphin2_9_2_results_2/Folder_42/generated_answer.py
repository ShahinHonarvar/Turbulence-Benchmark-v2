def gcf_three_nums(num_list):
    index1 = num_list[19]
    index2 = num_list[69]
    index3 = num_list[97]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_result = gcf(index1, index2)
    final_gcf = gcf(gcf_result, index3)
    return final_gcf