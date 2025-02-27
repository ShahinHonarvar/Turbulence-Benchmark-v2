def all_substring_of_size_n(the_str):
    if len(the_str) < 34:
        return []
    else:
        substring_lst = set()
        for i in range(len(the_str) - 33):
            for j in range(i + 1, len(the_str) - 32):
                for k in range(j + 1, len(the_str) - 31):
                    substring_lst.add(the_str[i:j + 1])
                    substring_lst.add(the_str[j:k + 1])
                    substring_lst.add(the_str[k:j + 34])
        return list(substring_lst)