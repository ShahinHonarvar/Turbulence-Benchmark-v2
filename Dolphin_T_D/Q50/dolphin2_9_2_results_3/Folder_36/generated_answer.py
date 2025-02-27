def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if len(my_list[i]) >= 3 and len(my_list[j]) >= 3:
                if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                    count += 1
    return count >= 312