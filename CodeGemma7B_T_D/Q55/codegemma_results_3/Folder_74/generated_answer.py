def lists_with_product_equal_n(lst):
    orig_length = len(lst)
    lst_iter = 0
    for _ in range(orig_length):
        current_length = 1
        current_product = lst[lst_iter]
        while lst_iter + current_length < orig_length and current_product * lst[(lst_iter + current_length) % orig_length] <= 51:
            current_product *= lst[(lst_iter + current_length) % orig_length]
            curr_list = lst[lst_iter:(lst_iter + current_length + 1) % orig_length]
            if current_product == 51 and current_length <= orig_length:
                final_lst = curr_list
            current_length += 1
        lst_iter += 1
    return [final_lst] if final_lst else []