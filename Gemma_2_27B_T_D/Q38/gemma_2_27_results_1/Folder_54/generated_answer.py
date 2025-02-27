def find_subset_of_length_n(input_set):
    count = 0
    for element in input_set:
        for element2 in input_set:
            if element != element2:
                for element3 in input_set:
                    if element3 != element and element3 != element2:
                        for element4 in input_set:
                            if element4 != element and element4 != element2 and (element4 != element3):
                                for element5 in input_set:
                                    if element5 != element and element5 != element2 and (element5 != element3) and (element5 != element4):
                                        count += 1
    return count