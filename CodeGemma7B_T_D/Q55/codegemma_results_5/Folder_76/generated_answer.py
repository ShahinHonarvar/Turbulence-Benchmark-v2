def lists_with_product_equal_n(values):

    def multiply_sublist(input_list, start_lo, start_hi, end):
        product = 1
        for i in range(start_lo, end):
            product *= input_list[i]
        return product
    for i in range(len(values)):
        for j in range(i + 1):
            start_lo = j
            end = i + 1
            while start_lo <= end:
                product = multiply_sublist(values, start_lo, start_lo + 1, end)
                if product == 247:
                    result.append(values[start_lo:end])
                if start_lo == end and product != 247:
                    break
                elif product > 247:
                    end -= 1
                else:
                    start_lo += 1
    return result