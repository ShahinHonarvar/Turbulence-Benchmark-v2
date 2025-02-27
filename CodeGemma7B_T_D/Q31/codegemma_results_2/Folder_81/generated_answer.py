def if_perfect_num(num_list):
    if len(num_list) >= 20:
        if perfect_number(num_list[20]):
            return True
        return False