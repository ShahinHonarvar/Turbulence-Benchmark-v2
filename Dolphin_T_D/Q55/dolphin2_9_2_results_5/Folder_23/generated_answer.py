def lists_with_product_equal_n(circular):
    result = []
    for i in range(len(circular)):
        for j in range(i + 1, len(circular) + 1):
            if i > j:
                continue
            elif ''.join(map(str, circular[i:j])) in circular[j:] + circular[:i]:
                product = 1
                for k in range(len(circular[i:j])):
                    product *= circular[i + k]
                if product == -95:
                    result.append(circular[i:j])
    return result