def find_original_set(set01, set02, set03, set04, set05, set06, set07, set08, set09, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29):
    original_set = set()
    for this_set in [set01, set02, set03, set04, set05, set06, set07, set08, set09, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29]:
        for number in this_set:
            if number not in original_set:
                original_set.add(number)
    return original_set