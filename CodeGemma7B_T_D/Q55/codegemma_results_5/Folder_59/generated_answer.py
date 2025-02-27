def lists_with_product_equal_n(given_list):
    for i in range(len(given_list)):
        current_list = [given_list[i]]
        current_product = given_list[i]
        for j in range(i + 1, len(given_list)):
            if current_product == -3:
                return [current_list]
            current_product *= given_list[j]
            current_list.append(given_list[j])
    return []